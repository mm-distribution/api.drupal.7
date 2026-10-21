# AJAXElementValidation::testAJAXElementValidation()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 611–620 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L611-L620)
- **Class:** [AJAXElementValidation](../AJAXElementValidation.md)
- **Module/theme:** batch_test

## Signature

```php
function testAJAXElementValidation()
```

## Documentation

```text
Try to post an Ajax change to a form that has a validated element.

The drivertext field is Ajax-enabled. An additional field is not, but
is set to be a required field. In this test the required field is not
filled in, and we want to see if the activation of the "drivertext"
Ajax-enabled field fails due to the required field being empty.
```

## Code

```php
  function testAJAXElementValidation() {
    $web_user = $this->drupalCreateUser();
    $edit = array('drivertext' => t('some dumb text'));

    // Post with 'drivertext' as the triggering element.
    $post_result = $this->drupalPostAJAX('ajax_validation_test', $edit, 'drivertext');
    // Look for a validation failure in the resultant JSON.
    $this->assertNoText(t('Error message'), "No error message in resultant JSON");
    $this->assertText('ajax_forms_test_validation_form_callback invoked', 'The correct callback was invoked');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
