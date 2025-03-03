# Running Atomic Tests

In order to run tests using `atomic-operator` you must have one or more [atomic tests](atomics.md).

## Selecting Tests to Run

By default, `atomic-operator` will run all known tests within the provided directory.

If you would like to specify specific tests then you must provide them as a list as input.

> Please note that techniques passed in but be separated by a `,` and __NO__ spaces.

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1560.002,T1560.001
```

## Checking Dependencies

There is an optional paramater that determines if `atomic-operator` should check dependencies or not. By default we do not check dependenicies but if set to `True` we will.

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1560.002,T1560.001 --check_dependicies True
```

Checking of dependencies means we will run any defined `prereq_command` defined within the Atomic test. 

## Get Prerequisities

Another optional paramater deteremines if we retrieve or run any `get_prereq_command` values defined within the Atomic test.

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1560.002,T1560.001  --check_dependencies True --get_prereq_command True
```

Setting this value to `True` means we will run that command but __only__ if `check_dependencies` is set to `True` as well. 

## Cleanup

This optional parameter is by default set to `False` but if set to `True` then we will run any `cleanup_command` values defined within an Atomic test.

```bash
atomic-operator run --atomics-path "~/_Swimlane/ atomic-red-team" --techniques T1560.002,T1560.001 --cleanup True
```

## Command Timeout

The `command_timeout` parameter tells `atomic-operator` the duration (in seconds) to run a command without exiting that process.

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1560.002,T1560.001 --command_timeout 40
```

This defaults to `20` seconds but you can specify another value if needed.

## Debug

The `debug` parameter will show additional details about the Atomic and tests (e.g. descriptions, etc.).

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1560.002,T1560.001 --debug
```

The default value is `False` and must be set to `True` to show this extra detail.

## Interactive Argument Inputs

The `prompt_for_input_args` parameter will enable an interactive session and prompt you to enter arguments for any Atomic test(s) that require input arguments. You can simply provide a value or select to use the `default` defined within the Atomic test.

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1560.002,T1560.001 --prompt_for_input_args True
```

The default value is `False` and must be set to `True` to prompt you for input values.

## kwargs

If you choose __not__ to set `prompt_for_input_args` to `True` then you can provide a dictionary of arguments in the `kwargs` input. This dictionary is only used for setting input argument values.  

For example, if you were running the Atomic test [T1564.001](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml) then would pass in a dictionary into the kwargs argument.

### Additional Input Arguments from Command Line

If you do not want `atomic-operator` to prompt you for inputs you can simply run the following on the command line:

```bash
atomic-operator run --atomics-path "~/_Swimlane/atomic-red-team" --techniques T1564.001 --kwargs '{"filename": "myscript.py"}'
```

