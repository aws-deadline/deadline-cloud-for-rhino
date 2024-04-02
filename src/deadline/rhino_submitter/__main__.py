# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
import sys
import os

deadline_rhino = sys.argv[-2]
deadline_rhino_path = os.path.dirname(deadline_rhino)
if deadline_rhino_path not in sys.path:
    sys.path.append(deadline_rhino_path)


if __name__ == "__main__":
    from rhino_submitter.rhino_render_submitter import show_submitter  # type: ignore

    show_submitter(sys.argv[-1])
