# simpletest_script_print_alternatives()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 855–869 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L855-L869)

## Signature

```php
function simpletest_script_print_alternatives($string, $array, $degree = 4)
```

## Documentation

```text
Prints alternative test names.

Searches the provided array of string values for close matches based on the
Levenshtein algorithm.

@see http://php.net/manual/en/function.levenshtein.php

@param string $string
  A string to test.
@param array $array
  A list of strings to search.
@param int $degree
  The matching strictness. Higher values return fewer matches. A value of
  4 means that the function will return strings from $array if the candidate
  string in $array would be identical to $string by changing 1/4 or fewer of
  its characters.
```

## Code

```php
function simpletest_script_print_alternatives($string, $array, $degree = 4) {
  $alternatives = array();
  foreach ($array as $item) {
    $lev = levenshtein($string, $item);
    if ($lev <= strlen($item) / $degree || FALSE !== strpos($string, $item)) {
      $alternatives[] = $item;
    }
  }
  if (!empty($alternatives)) {
    simpletest_script_print("  Did you mean?\n", SIMPLETEST_SCRIPT_COLOR_FAIL);
    foreach ($alternatives as $alternative) {
      simpletest_script_print("  - $alternative\n", SIMPLETEST_SCRIPT_COLOR_FAIL);
    }
  }
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
