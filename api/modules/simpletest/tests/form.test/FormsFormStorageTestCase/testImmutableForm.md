# FormsFormStorageTestCase::testImmutableForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1395–1420 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1395-L1420)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testImmutableForm()
```

## Documentation

```text
Verifies that form build-id is regenerated when loading an immutable form
from the cache.
```

## Code

```php
  function testImmutableForm() {
    // Request the form with 'cache' query parameter to enable form caching.
    $this->drupalGet('form_test/form-storage', array('query' => array('cache' => 1, 'immutable' => 1)));
    $buildIdFields = $this->xpath('//input[@name="form_build_id"]');
    $this->assertEqual(count($buildIdFields), 1, 'One form build id field on the page');
    $buildId = (string) $buildIdFields[0]['value'];

    // Trigger validation error by submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Continue submit');

    // Verify that the build-id did change.
    $this->assertNoFieldByName('form_build_id', $buildId, 'Build id changes when form validation fails');

    // Retrieve the new build-id.
    $buildIdFields = $this->xpath('//input[@name="form_build_id"]');
    $this->assertEqual(count($buildIdFields), 1, 'One form build id field on the page');
    $buildId = (string) $buildIdFields[0]['value'];

    // Trigger validation error by again submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Continue submit');

    // Verify that the build-id does not change the second time.
    $this->assertFieldByName('form_build_id', $buildId, 'Build id remains the same when form validation fails subsequently');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
