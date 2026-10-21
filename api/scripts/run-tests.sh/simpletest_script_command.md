# simpletest_script_command()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 467–483 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L467-L483)

## Signature

```php
function simpletest_script_command($test_id, $test_class)
```

## Documentation

```text
Return a command used to run a test in a separate process.

@param $test_id
 The current test ID.
@param $test_class
 The name of the test class to run.
```

## Code

```php
function simpletest_script_command($test_id, $test_class) {
  global $args, $php;

  $command = escapeshellarg($php) . ' ' . escapeshellarg('./scripts/' . $args['script']) . ' --url ' . escapeshellarg($args['url']);
  if ($args['color']) {
    $command .= ' --color';
  }
  if ($args['cache-modules']) {
    $command .= ' --cache --cache-modules';
  }
  elseif ($args['cache']) {
    $command .= ' --cache';
  }

  $command .= " --php " . escapeshellarg($php) . " --test-id $test_id --execute-test " . escapeshellarg($test_class);
  return $command;
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
