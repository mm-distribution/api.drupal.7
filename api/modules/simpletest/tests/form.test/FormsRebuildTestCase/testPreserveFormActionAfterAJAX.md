# FormsRebuildTestCase::testPreserveFormActionAfterAJAX()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1772–1814 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1772-L1814)
- **Class:** [FormsRebuildTestCase](../FormsRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testPreserveFormActionAfterAJAX()
```

## Documentation

```text
Tests that a form's action is retained after an Ajax submission.

The 'action' attribute of a form should not change after an Ajax submission
followed by a non-Ajax submission, which triggers a validation error.
```

## Code

```php
  function testPreserveFormActionAfterAJAX() {
    // Create a multi-valued field for 'page' nodes to use for Ajax testing.
    $field_name = 'field_ajax_test';
    $field = array(
      'field_name' => $field_name,
      'type' => 'text',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
    );
    field_create_field($field);
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'node',
      'bundle' => 'page',
    );
    field_create_instance($instance);

    // Log in a user who can create 'page' nodes.
    $this->web_user = $this->drupalCreateUser(array('create page content'));
    $this->drupalLogin($this->web_user);

    // Get the form for adding a 'page' node. Submit an "add another item" Ajax
    // submission and verify it worked by ensuring the updated page has two text
    // field items in the field for which we just added an item.
    $this->drupalGet('node/add/page');
    $this->drupalPostAJAX(NULL, array(), array('field_ajax_test_add_more' => t('Add another item')), 'system/ajax', array(), array(), 'page-node-form');
    $this->assert(count($this->xpath('//div[contains(@class, "field-name-field-ajax-test")]//input[@type="text"]')) == 2, 'AJAX submission succeeded.');

    // Submit the form with the non-Ajax "Save" button, leaving the title field
    // blank to trigger a validation error, and ensure that a validation error
    // occurred, because this test is for testing what happens when a form is
    // re-rendered without being re-built, which is what happens when there's
    // a validation error.
    $this->drupalPost(NULL, array(), t('Save'));
    $this->assertText('Title field is required.', 'Non-AJAX submission correctly triggered a validation error.');

    // Ensure that the form contains two items in the multi-valued field, so we
    // know we're testing a form that was correctly retrieved from cache.
    $this->assert(count($this->xpath('//form[contains(@id, "page-node-form")]//div[contains(@class, "form-item-field-ajax-test")]//input[@type="text"]')) == 2, 'Form retained its state from cache.');

    // Ensure that the form's action is correct.
    $forms = $this->xpath('//form[contains(@class, "node-page-form")]');
    $this->assert(count($forms) == 1 && $forms[0]['action'] == url('node/add/page'), 'Re-rendered form contains the correct action value.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
