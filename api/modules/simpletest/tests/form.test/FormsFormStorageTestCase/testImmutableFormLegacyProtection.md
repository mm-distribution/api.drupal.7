# FormsFormStorageTestCase::testImmutableFormLegacyProtection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1425–1446 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1425-L1446)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testImmutableFormLegacyProtection()
```

## Documentation

```text
Verify that existing contrib code cannot overwrite immutable form state.
```

## Code

```php
  public function testImmutableFormLegacyProtection() {
    $this->drupalGet('form_test/form-storage', array('query' => array('cache' => 1, 'immutable' => 1)));
    $build_id_fields = $this->xpath('//input[@name="form_build_id"]');
    $this->assertEqual(count($build_id_fields), 1, 'One form build id field on the page');
    $build_id = (string) $build_id_fields[0]['value'];

    // Try to poison the form cache.
    $original = $this->drupalGetAJAX('form_test/form-storage-legacy/' . $build_id);
    $this->assertEqual($original['form']['#build_id_old'], $build_id, 'Original build_id was recorded');
    $this->assertNotEqual($original['form']['#build_id'], $build_id, 'New build_id was generated');

    // Assert that a watchdog message was logged by form_set_cache.
    $status = (bool) db_query_range('SELECT 1 FROM {watchdog} WHERE message = :message', 0, 1, array(':message' => 'Form build-id mismatch detected while attempting to store a form in the cache.'));
    $this->assert($status, 'A watchdog message was logged by form_set_cache');

    // Ensure that the form state was not poisoned by the preceeding call.
    $original = $this->drupalGetAJAX('form_test/form-storage-legacy/' . $build_id);
    $this->assertEqual($original['form']['#build_id_old'], $build_id, 'Original build_id was recorded');
    $this->assertNotEqual($original['form']['#build_id'], $build_id, 'New build_id was generated');
    $this->assert(empty($original['form']['#poisoned']), 'Original form structure was preserved');
    $this->assert(empty($original['form_state']['poisoned']), 'Original form state was preserved');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
