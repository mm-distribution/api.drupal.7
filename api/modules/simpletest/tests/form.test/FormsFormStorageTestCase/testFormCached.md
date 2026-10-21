# FormsFormStorageTestCase::testFormCached()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1278–1297 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1278-L1297)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFormCached()
```

## Documentation

```text
Tests using the form with an activated $form_state['cache'] property.
```

## Code

```php
  function testFormCached() {
    $this->drupalGet('form_test/form-storage', array('query' => array('cache' => 1)));
    $this->assertText('Form constructions: 1');

    $edit = array('title' => 'new', 'value' => 'value_is_set');

    // Use form rebuilding triggered by a submit button.
    $this->drupalPost(NULL, $edit, 'Continue submit');
    $this->assertText('Form constructions: 2');

    // Reset the form to the values of the storage, using a form rebuild
    // triggered by button of type button.
    $this->drupalPost(NULL, array('title' => 'changed'), 'Reset');
    $this->assertFieldByName('title', 'new', 'Values have been resetted.');
    $this->assertText('Form constructions: 3');

    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertText('Form constructions: 3');
    $this->assertText('Title: new', 'The form storage has stored the values.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
