# FormsProgrammaticTestCase::testSubmissionWorkflow()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1912–1953 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1912-L1953)
- **Class:** [FormsProgrammaticTestCase](../FormsProgrammaticTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSubmissionWorkflow()
```

## Documentation

```text
Test the programmatic form submission workflow.
```

## Code

```php
  function testSubmissionWorkflow() {
    // Backup the current batch status and reset it to avoid conflicts while
    // processing the dummy form submit handler.
    $current_batch = $batch =& batch_get();
    $batch = array();

    // Test that a programmatic form submission is rejected when a required
    // textfield is omitted and correctly processed when it is provided.
    $this->submitForm(array(), FALSE);
    $this->submitForm(array('textfield' => 'test 1'), TRUE);
    $this->submitForm(array(), FALSE);
    $this->submitForm(array('textfield' => 'test 2'), TRUE);

    // Test that a programmatic form submission can turn on and off checkboxes
    // which are, by default, checked.
    $this->submitForm(array('textfield' => 'dummy value', 'checkboxes' => array(1 => 1, 2 => 2)), TRUE);
    $this->submitForm(array('textfield' => 'dummy value', 'checkboxes' => array(1 => 1, 2 => NULL)), TRUE);
    $this->submitForm(array('textfield' => 'dummy value', 'checkboxes' => array(1 => NULL, 2 => 2)), TRUE);
    $this->submitForm(array('textfield' => 'dummy value', 'checkboxes' => array(1 => NULL, 2 => NULL)), TRUE);

    // Test that a programmatic form submission can successfully submit values
    // even for fields where the #access property is FALSE.
    $this->submitForm(array('textfield' => 'dummy value', 'textfield_no_access' => 'test value'), TRUE);
    // Test that #access is respected for programmatic form submissions when
    // requested to do so.
    $submitted_values = array('textfield' => 'dummy value', 'textfield_no_access' => 'test value');
    $expected_values = array('textfield' => 'dummy value', 'textfield_no_access' => 'default value');
    $form_state = array('programmed_bypass_access_check' => FALSE);
    $this->submitForm($submitted_values, TRUE, $expected_values, $form_state);

    // Test that a programmatic form submission can correctly click a button
    // that limits validation errors based on user input. Since we do not
    // submit any values for "textfield" here and the textfield is required, we
    // only expect form validation to pass when validation is limited to a
    // different field.
    $this->submitForm(array('op' => 'Submit with limited validation', 'field_to_validate' => 'all'), FALSE);
    $this->submitForm(array('op' => 'Submit with limited validation', 'field_to_validate' => 'textfield'), FALSE);
    $this->submitForm(array('op' => 'Submit with limited validation', 'field_to_validate' => 'field_to_validate'), TRUE);

    // Restore the current batch status.
    $batch = $current_batch;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
