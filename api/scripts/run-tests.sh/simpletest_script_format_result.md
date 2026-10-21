# simpletest_script_format_result()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 778–790 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L778-L790)

## Signature

```php
function simpletest_script_format_result($result)
```

## Documentation

```text
Format the result so that it fits within the default 80 character
terminal size.

@param $result The result object to format.
```

## Code

```php
function simpletest_script_format_result($result) {
  global $results_map, $color;

  $summary = sprintf("%-9.9s %-10.10s %-17.17s %4.4s %-35.35s\n",
    $results_map[$result->status], $result->message_group, basename($result->file), $result->line, $result->function);

  simpletest_script_print($summary, simpletest_script_color_code($result->status));

  $lines = explode("\n", wordwrap(trim(strip_tags($result->message)), 76));
  foreach ($lines as $line) {
    echo "    $line\n";
  }
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
