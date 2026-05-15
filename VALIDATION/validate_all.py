#!/usr/bin/env python3
import argparse, runpy, sys, os
from pathlib import Path
root = Path(__file__).resolve().parents[1]
validators = [
    'validate_no_stale_root_placeholders.py',
    'validate_clean_engine_root.py',
    'validate_feature_manifest.py',
    'validate_skill_layer.py',
    'validate_engine_structure.py',
    'validate_source_of_truth_rules.py',
]
optional = [
    'validate_runtime_infrastructure_layer.py',
    'validate_project_injection_layer.py',
    'validate_cleanup_command.py',
    'validate_project_adoption_and_git_boundaries.py',
    'validate_git_provider_integrations.py',
    'validate_doc_source_integrations.py',
    'validate_source_pipeline_orchestrator.py',
    'validate_code_context_sources.py',
    'validate_appforger_mcp_server.py',
    'validate_integration_strategy_advisor.py',
]
validators += [v for v in optional if (root / 'validation' / v).exists()]
parser = argparse.ArgumentParser()
parser.add_argument('--deep', action='store_true')
parser.add_argument('--timeout', type=int, default=60, help='Reserved for subprocess validators.')
args = parser.parse_args()
old_cwd = os.getcwd()
os.chdir(root)
try:
    for v in validators:
        p = root / 'validation' / v
        print('RUN', v, flush=True)
        old_argv = sys.argv[:]
        sys.argv = [str(p)]
        if args.deep and v in {'validate_source_pipeline_orchestrator.py'}:
            sys.argv.append('--deep')
        try:
            runpy.run_path(str(p), run_name='__main__')
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 1
            if code:
                print(f'{v} failed with exit code {code}')
                raise
        finally:
            sys.argv = old_argv
finally:
    os.chdir(old_cwd)
print('validate_all: OK')
