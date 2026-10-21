# simpletest_script_execute_batch()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 357–413 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L357-L413)

## Signature

```php
function simpletest_script_execute_batch($test_id, $test_classes)
```

## Documentation

```text
Execute a batch of tests.
```

## Code

```php
function simpletest_script_execute_batch($test_id, $test_classes) {
  global $args;

  $total_status = SIMPLETEST_SCRIPT_EXIT_SUCCESS;

  // Multi-process execution.
  $children = array();
  while (!empty($test_classes) || !empty($children)) {
    while (count($children) < $args['concurrency']) {
      if (empty($test_classes)) {
        break;
      }

      // Fork a child process.
      $test_class = array_shift($test_classes);
      $command = simpletest_script_command($test_id, $test_class);
      $process = proc_open($command, array(), $pipes, NULL, NULL, array('bypass_shell' => TRUE));

      if (!is_resource($process)) {
        echo "Unable to fork test process. Aborting.\n";
        exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
      }

      // Register our new child.
      $children[] = array(
        'process' => $process,
        'class' => $test_class,
        'pipes' => $pipes,
      );
    }

    // Wait for children every 200ms.
    usleep(200000);

    // Check if some children finished.
    foreach ($children as $cid => $child) {
      $status = proc_get_status($child['process']);
      if (empty($status['running'])) {
        // The child exited, unregister it.
        proc_close($child['process']);
        if ($status['exitcode'] == SIMPLETEST_SCRIPT_EXIT_FAILURE) {
          if ($status['exitcode'] > $total_status) {
            $total_status = $status['exitcode'];
          }
        }
        elseif ($status['exitcode']) {
          $total_status = $status['exitcode'];
          echo 'FATAL ' . $test_class . ': test runner returned a non-zero error code (' . $status['exitcode'] . ').' . "\n";
        }

        // Remove this child.
        unset($children[$cid]);
      }
    }
  }
  return $total_status;
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
