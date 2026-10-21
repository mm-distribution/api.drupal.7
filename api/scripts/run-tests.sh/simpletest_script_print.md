# simpletest_script_print()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 809–817 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L809-L817)

## Signature

```php
function simpletest_script_print($message, $color_code)
```

## Documentation

```text
Print a message to the console, if color is enabled then the specified
color code will be used.

@param $message The message to print.
@param $color_code The color code to use for coloring.
```

## Code

```php
function simpletest_script_print($message, $color_code) {
  global $args;
  if (!empty($args['color'])) {
    echo "\033[" . $color_code . "m" . $message . "\033[0m";
  }
  else {
    echo $message;
  }
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
