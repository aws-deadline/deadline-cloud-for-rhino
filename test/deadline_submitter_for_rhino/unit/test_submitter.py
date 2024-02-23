# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
from __future__ import annotations
from pathlib import Path
import yaml
import tempfile
import deadline.rhino_submitter.rhino_render_submitter as submitter_module
from deadline.rhino_submitter.data_classes import RenderSubmitterUISettings


def test_render_settings():
    a = RenderSubmitterUISettings()
    _, path = tempfile.mkstemp(suffix="json", text=True)
    a.save_sticky_settings(path)
    b = RenderSubmitterUISettings()
    b.load_sticky_settings(path)
    assert a.submitter_name == b.submitter_name
    assert a.description == b.description
    assert a.frame_list == b.frame_list
    assert a.output_file_path == b.output_file_path
    assert a.input_filenames == b.input_filenames
    assert a.input_directories == b.input_directories


def test_get_job_template():
    module_dir = Path(submitter_module.__file__).parent
    with open(module_dir / "default_rhino_job_template.yaml") as fh:
        default_job_template = yaml.safe_load(fh)
    settings = RenderSubmitterUISettings()
    settings.output_file_path = "/tmp/foo.%d.tif"
    job_template = submitter_module._get_job_template(
        default_job_template,
        settings,
    )
    assert job_template["steps"]


def test_get_parameter_values():
    settings = RenderSubmitterUISettings()
    queue = []
    frames = "1-5"
    scene_name = "foo"
    params = submitter_module._get_parameter_values(settings, queue, frames, scene_name)
    assert params is not None
    for param in params:
        if param["name"] == "Frames":
            assert param["value"] == "1-5"
        if param["name"] == "RhinoFile":
            assert param["value"] == "foo"
