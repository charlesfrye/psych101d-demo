import argparse
import os.path
import re
import sys

import nbformat
import nbconvert.preprocessors

DEFAULT_LINTER = "flake8"


def main(preprocessor_str, notebook_paths):
    preprocessors = PREPROCESSORS[preprocessor_str]
    if preprocessor_str in ["to_student", "add_magic", "lint"]:
        output_paths = [make_output_path(notebook_path, preprocessor_str)
                        for notebook_path in notebook_paths]
    else:
        output_paths = notebook_paths

    for notebook_path, output_path in zip(notebook_paths, output_paths):
        do_preprocessing(preprocessors, notebook_path, output_path)


def do_preprocessing(preprocessors, notebook_path, output_path):

    output_directory = os.path.dirname(output_path)

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    print("Preprocessing {0}".format(notebook_path))

    resources = {'metadata': {'path': output_directory}}
    for preprocessor in preprocessors:
        try:
            if hasattr(preprocessor, "cellwise") and preprocessor.cellwise:
                resources = run_cellwise_preprocessor(
                    preprocessor, nb, resources)
            else:
                preprocessor.preprocess(nb, resources)
            if "report" in resources.keys():
                if len(resources["report"].split("\n")) > 1:
                    print(resources["report"])
        except nbconvert.preprocessors.CellExecutionError:
            error_msg = "\033[1;31mError Executing Notebook {}\033[0m".format(
                        notebook_path)
            print("\t" + error_msg)

    with open(output_path, 'wt') as f:
        nbformat.write(nb, f)

    print("\tSaved to {0}".format(output_path))


class AddMagicPreprocessor(nbconvert.preprocessors.Preprocessor):

    def __init__(self, *args, linter_str=DEFAULT_LINTER, **kwargs):
        super().__init__(*args, **kwargs)

        self.loading_magic_str = "%load_ext pycodestyle_magic\n"
        self.linter_str = linter_str
        self.linter_magic_str = "%%{}\n".format(linter_str)

        self.preprocessed_first_code_cell = False

        self.cellwise = True

    def preprocess_cell(self, cell, resources, index):

        if cell["cell_type"] == "code":
            if not self.preprocessed_first_code_cell:
                self.preprocessed_first_code_cell = True
                magic_str = self.loading_magic_str
            else:
                magic_str = self.linter_magic_str

            self.add_magic(cell, magic_str)

        return cell, resources

    def add_magic(self, cell, magic_str):
        cell_source = cell["source"]

        if not cell_source.startswith(magic_str):
            # do not lint cells with magic in them
            if not cell_source.startswith("%") &\
                   (magic_str == self.linter_magic_str):
                cell_source = magic_str + cell_source

        cell["source"] = cell_source


class ReportLintPreprocessor(nbconvert.preprocessors.Preprocessor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cellwise = True

    def preprocess_cell(self, cell, resources, index):

        self.report_linting(cell, resources, index)

        return cell, resources

    def report_linting(self, cell, resources, index):

        stderrs = self.extract_stderrs(cell)
        if stderrs == []:
            return

        linterrs = self.filter_to_linterrs(stderrs)

        self.add_to_report(linterrs, resources, index)

    @staticmethod
    def add_to_report(linterrs, resources, index):
        if "report" not in resources.keys():
            resources["report"] = "\tLinting Errors:"

        for linterr in linterrs:
            resources["report"] += "\n\t\t" + str(index) + ":" + linterr

    @staticmethod
    def extract_stderrs(cell):
        stderrs = []
        if "outputs" in cell.keys():
            outputs = cell["outputs"]
        else:
            outputs = []

        for output in outputs:
            if "name" in output.keys():
                if output["name"] == "stderr":
                    stderrs.append(output["text"].strip())

        return stderrs

    def filter_to_linterrs(self, stderrs):
        linterrs = [stderr for stderr in stderrs
                    if self.is_linterr(stderr)]

        return linterrs

    @staticmethod
    def is_linterr(err):
        pattern = r"([0-9]+:){1,2} [EW][0-9]{3}"
        return re.match(pattern, err)


def run_cellwise_preprocessor(cw_preprocessor, nb, resources=None):

    if resources is None:
        resources = {}

    for idx, cell in enumerate(nb["cells"]):
        cw_preprocessor.preprocess_cell(cell, resources, idx)

    return resources


def make_execute_preprocessor():
    ep = nbconvert.preprocessors.ExecutePreprocessor(
        timeout=600, kernel_name='python3')
    return ep


def make_remove_answers_preprocessor():
    text_answer_pattern = r"""<font color=['"]#?1874CD['"]>"""
    code_answer_pattern = r"""#* answer"""
    rap = nbconvert.preprocessors.RegexRemovePreprocessor(
        patterns=[code_answer_pattern,
                  text_answer_pattern,
                  ])
    return rap


def make_to_student_preprocessors():
    tsps = [make_clear_output_preprocessor(),
            make_remove_answers_preprocessor()
            ]
    return tsps


def make_clear_output_preprocessor():
    cop = nbconvert.preprocessors.ClearOutputPreprocessor()
    return cop


def make_add_magic_preprocessor():
    amp = AddMagicPreprocessor()
    return amp


def make_report_lint_preprocessor():
    rlp = ReportLintPreprocessor()
    return rlp


def make_lint_preprocessors():
    mlps = [make_add_magic_preprocessor(),
            make_execute_preprocessor(),
            make_report_lint_preprocessor()
            ]
    return mlps


def make_output_path(notebook_path, preprocessor_str):
    dirname, basename = os.path.split(notebook_path)

    if preprocessor_str == "to_student":
        newbasename = ''.join(basename.split(" - Solutions"))
    elif preprocessor_str in ["add_magic", "lint"]:
        basename_split = basename.split(".")
        newbasename = '.'.join(basename_split[:-1]
                               + ["lint"] + basename_split[-1:])
    else:
        raise ValueError("preprocessor_str {} not understood"
                         .format(preprocessor_str))

    return os.path.join(dirname, newbasename)


PREPROCESSORS = {"execute": [make_execute_preprocessor()],
                 "remove_answers": [make_remove_answers_preprocessor()],
                 "clear_output": [make_clear_output_preprocessor()],
                 "to_student": make_to_student_preprocessors(),
                 "add_magic": [make_add_magic_preprocessor()],
                 "lint": make_lint_preprocessors()
                 }


def build_parser():
    parser = argparse.ArgumentParser(
        description="Apply preprocessing to notebooks. "
        "Options include executing notebooks, clearing outputs,"
        "converting to student versions, and linting.")
    parser.add_argument(
        "preprocessor", choices=PREPROCESSORS.keys(),
        help="String identifying type of preprocessing to run.")
    parser.add_argument(
        "notebook_paths", nargs="+",
        help="One or more paths to notebooks on which to run preprocessing.")
    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    preprocessor_str = args.preprocessor
    assert preprocessor_str in PREPROCESSORS.keys(), \
        "preprocessor_str not understood"
    notebook_paths = args.notebook_paths
    sys.exit(main(preprocessor_str, notebook_paths))
