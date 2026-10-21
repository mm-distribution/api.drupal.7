# field_test_memorize()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 164–175 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L164-L175)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_memorize($key = NULL, $value = NULL)
```

## Documentation

```text
Store and retrieve keyed data for later verification by unit tests.

This function is a simple in-memory key-value store with the
distinction that it stores all values for a given key instead of
just the most recently set value. field_test module hooks call
this function to record their arguments, keyed by hook name. The
unit tests later call this function to verify that the correct
hooks were called and were passed the correct arguments.

This function ignores all calls until the first time it is called
with $key of NULL. Each time it is called with $key of NULL, it
erases all previously stored data from its internal cache, but also
returns the previously stored data to the caller. A typical usage
scenario is:

@code
  // calls to field_test_memorize() here are ignored

  // turn on memorization
  field_test_memorize();

  // call some Field API functions that invoke field_test hooks
  $field = field_create_field(...);

  // retrieve and reset the memorized hook call data
  $mem = field_test_memorize();

  // make sure hook_field_create_field() is invoked correctly
  assertEqual(count($mem['field_test_field_create_field']), 1);
  assertEqual($mem['field_test_field_create_field'][0], array($field));
@endcode

@param $key
  The key under which to store to $value, or NULL as described above.
@param $value
  A value to store for $key.
@return
  An array mapping each $key to an array of each $value passed in
  for that key.
```

## Code

```php
function field_test_memorize($key = NULL, $value = NULL) {
  $memorize = &drupal_static(__FUNCTION__, NULL);

  if (!isset($key)) {
    $return = $memorize;
    $memorize = array();
    return $return;
  }
  if (is_array($memorize)) {
    $memorize[$key][] = $value;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
