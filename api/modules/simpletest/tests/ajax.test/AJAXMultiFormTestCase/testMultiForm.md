# AJAXMultiFormTestCase::testMultiForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 475–509 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L475-L509)
- **Class:** [AJAXMultiFormTestCase](../AJAXMultiFormTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultiForm()
```

## Documentation

```text
Test that a page with the 'page_node_form' included twice works correctly.
```

## Code

```php
  function testMultiForm() {
    // HTML IDs for elements within the field are potentially modified with
    // each Ajax submission, but these variables are stable and help target the
    // desired elements.
    $field_name = 'field_ajax_test';
    $field_xpaths = array(
      'page-node-form' => '//form[@id="page-node-form"]//div[contains(@class, "field-name-field-ajax-test")]',
      'page-node-form--2' => '//form[@id="page-node-form--2"]//div[contains(@class, "field-name-field-ajax-test")]',
    );
    $button_name = $field_name . '_add_more';
    $button_value = t('Add another item');
    $button_xpath_suffix = '//input[@name="' . $button_name . '"]';
    $field_items_xpath_suffix = '//input[@type="text"]';

    // Ensure the initial page contains both node forms and the correct number
    // of field items and "add more" button for the multi-valued field within
    // each form.
    $this->drupalGet('form-test/two-instances-of-same-form');
    foreach ($field_xpaths as $form_html_id => $field_xpath) {
      $this->assert(count($this->xpath($field_xpath . $field_items_xpath_suffix)) == 1, t('Found the correct number of field items on the initial page.'));
      $this->assertFieldByXPath($field_xpath . $button_xpath_suffix, NULL, t('Found the "add more" button on the initial page.'));
    }
    $this->assertNoDuplicateIds(t('Initial page contains unique IDs'), 'Other');

    // Submit the "add more" button of each form twice. After each corresponding
    // page update, ensure the same as above.
    foreach ($field_xpaths as $form_html_id => $field_xpath) {
      for ($i = 0; $i < 2; $i++) {
        $this->drupalPostAJAX(NULL, array(), array($button_name => $button_value), 'system/ajax', array(), array(), $form_html_id);
        $this->assert(count($this->xpath($field_xpath . $field_items_xpath_suffix)) == $i+2, t('Found the correct number of field items after an AJAX submission.'));
        $this->assertFieldByXPath($field_xpath . $button_xpath_suffix, NULL, t('Found the "add more" button after an AJAX submission.'));
        $this->assertNoDuplicateIds(t('Updated page contains unique IDs'), 'Other');
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
