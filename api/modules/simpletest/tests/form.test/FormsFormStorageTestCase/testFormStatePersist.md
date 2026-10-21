# FormsFormStorageTestCase::testFormStatePersist()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1348–1370 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1348-L1370)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFormStatePersist()
```

## Documentation

```text
Tests a form using form state without using 'storage' to pass data from the
constructor to a submit handler. The data has to persist even when caching
gets activated, what may happen when a modules alter the form and adds
#ajax properties.
```

## Code

```php
  function testFormStatePersist() {
    // Test the form one time with caching activated and one time without.
    $run_options = array(
      array(),
      array('query' => array('cache' => 1)),
    );
    foreach ($run_options as $options) {
      $this->drupalPost('form-test/state-persist', array(), t('Submit'), $options);
      // The submit handler outputs the value in $form_state, assert it's there.
      $this->assertText('State persisted.');

      // Test it again, but first trigger a validation error, then test.
      $this->drupalPost('form-test/state-persist', array('title' => ''), t('Submit'), $options);
      $this->assertText(t('!name field is required.', array('!name' => 'title')));
      // Submit the form again triggering no validation error.
      $this->drupalPost(NULL, array('title' => 'foo'), t('Submit'), $options);
      $this->assertText('State persisted.');

      // Now post to the rebuilt form and verify it's still there afterwards.
      $this->drupalPost(NULL, array('title' => 'bar'), t('Submit'), $options);
      $this->assertText('State persisted.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
