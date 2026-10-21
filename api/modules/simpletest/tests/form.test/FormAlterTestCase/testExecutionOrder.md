# FormAlterTestCase::testExecutionOrder()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 628–640 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L628-L640)
- **Class:** [FormAlterTestCase](../FormAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testExecutionOrder()
```

## Documentation

```text
Tests execution order of hook_form_alter() and hook_form_FORM_ID_alter().
```

## Code

```php
  function testExecutionOrder() {
    $this->drupalGet('form-test/alter');
    // Ensure that the order is first by module, then for a given module, the
    // id-specific one after the generic one.
    $expected = array(
      'block_form_form_test_alter_form_alter() executed.',
      'form_test_form_alter() executed.',
      'form_test_form_form_test_alter_form_alter() executed.',
      'system_form_form_test_alter_form_alter() executed.',
    );
    $content = preg_replace('/\s+/', ' ', filter_xss($this->content, array()));
    $this->assert(strpos($content, implode(' ', $expected)) !== FALSE, 'Form alter hooks executed in the expected order.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
