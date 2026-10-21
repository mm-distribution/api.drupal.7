# FormStateValuesCleanAdvancedTestCase::testFormStateValuesCleanAdvanced()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1700–1718 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1700-L1718)
- **Class:** [FormStateValuesCleanAdvancedTestCase](../FormStateValuesCleanAdvancedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFormStateValuesCleanAdvanced()
```

## Documentation

```text
Tests form_state_values_clean().
```

## Code

```php
  function testFormStateValuesCleanAdvanced() {

    // Get an image for uploading.
    $image_files = $this->drupalGetTestFiles('image');
    $this->image = current($image_files);

    // Check if the physical file is there.
    $this->assertTrue(is_file($this->image->uri), "The image file we're going to upload exists.");

    // "Browse" for the desired file.
    $edit = array('files[image]' => drupal_realpath($this->image->uri));

    // Post the form.
    $this->drupalPost('form_test/form-state-values-clean-advanced', $edit, t('Submit'));

    // Expecting a 200 HTTP code.
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
