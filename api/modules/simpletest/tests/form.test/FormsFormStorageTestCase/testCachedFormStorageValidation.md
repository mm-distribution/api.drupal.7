# FormsFormStorageTestCase::testCachedFormStorageValidation()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1317–1340 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1317-L1340)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCachedFormStorageValidation()
```

## Documentation

```text
Tests updating cached form storage during form validation.

If form caching is enabled and a form stores data in the form storage, then
the form storage also has to be updated in case of a validation error in
the form. This test re-uses the existing form for multi-step tests, but
triggers a special #element_validate handler to update the form storage
during form validation, while another, required element in the form
triggers a form validation error.
```

## Code

```php
  function testCachedFormStorageValidation() {
    // Request the form with 'cache' query parameter to enable form caching.
    $this->drupalGet('form_test/form-storage', array('query' => array('cache' => 1)));

    // Skip step 1 of the multi-step form, since the first step copies over
    // 'title' into form storage, but we want to verify that changes in the form
    // storage are updated in the cache during form validation.
    $edit = array('title' => 'foo');
    $this->drupalPost(NULL, $edit, 'Continue submit');

    // In step 2, trigger a validation error for the required 'title' field, and
    // post the special 'change_title' value for the 'value' field, which
    // conditionally invokes the #element_validate handler to update the form
    // storage.
    $edit = array('title' => '', 'value' => 'change_title');
    $this->drupalPost(NULL, $edit, 'Save');

    // At this point, the form storage should contain updated values, but we do
    // not see them, because the form has not been rebuilt yet due to the
    // validation error. Post again and verify that the rebuilt form contains
    // the values of the updated form storage.
    $this->drupalPost(NULL, array('title' => 'foo', 'value' => 'bar'), 'Save');
    $this->assertText("The thing has been changed.", 'The altered form storage value was updated in cache and taken over.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
