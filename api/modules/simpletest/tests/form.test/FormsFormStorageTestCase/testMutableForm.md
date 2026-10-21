# FormsFormStorageTestCase::testMutableForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1376–1389 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1376-L1389)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMutableForm()
```

## Documentation

```text
Verify that the form build-id remains the same when validation errors
occur on a mutable form.
```

## Code

```php
  function testMutableForm() {
    // Request the form with 'cache' query parameter to enable form caching.
    $this->drupalGet('form_test/form-storage', array('query' => array('cache' => 1)));
    $buildIdFields = $this->xpath('//input[@name="form_build_id"]');
    $this->assertEqual(count($buildIdFields), 1, 'One form build id field on the page');
    $buildId = (string) $buildIdFields[0]['value'];

    // Trigger validation error by submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Continue submit');

    // Verify that the build-id did not change.
    $this->assertFieldByName('form_build_id', $buildId, 'Build id remains the same when form validation fails');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
