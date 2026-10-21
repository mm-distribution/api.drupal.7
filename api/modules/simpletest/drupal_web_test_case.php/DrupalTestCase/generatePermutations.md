# DrupalTestCase::generatePermutations()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 729–745 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L729-L745)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function generatePermutations($parameters)
```

## Documentation

```text
Converts a list of possible parameters into a stack of permutations.

Takes a list of parameters containing possible values, and converts all of
them into a list of items containing every possible permutation.

Example:
@code
$parameters = array(
  'one' => array(0, 1),
  'two' => array(2, 3),
);
$permutations = DrupalTestCase::generatePermutations($parameters)
// Result:
$permutations == array(
  array('one' => 0, 'two' => 2),
  array('one' => 1, 'two' => 2),
  array('one' => 0, 'two' => 3),
  array('one' => 1, 'two' => 3),
)
@endcode

@param $parameters
  An associative array of parameters, keyed by parameter name, and whose
  values are arrays of parameter values.

@return
  A list of permutations, which is an array of arrays. Each inner array
  contains the full list of parameters that have been passed, but with a
  single value only.
```

## Code

```php
  public static function generatePermutations($parameters) {
    $all_permutations = array(array());
    foreach ($parameters as $parameter => $values) {
      $new_permutations = array();
      // Iterate over all values of the parameter.
      foreach ($values as $value) {
        // Iterate over all existing permutations.
        foreach ($all_permutations as $permutation) {
          // Add the new parameter value to existing permutations.
          $new_permutations[] = $permutation + array($parameter => $value);
        }
      }
      // Replace the old permutations with the new permutations.
      $all_permutations = $new_permutations;
    }
    return $all_permutations;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
