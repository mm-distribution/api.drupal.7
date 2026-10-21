# BatchPageTestCase::testBatchProgressPageTheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 296–312 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L296-L312)
- **Class:** [BatchPageTestCase](../BatchPageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchProgressPageTheme()
```

## Documentation

```text
Tests that the batch API progress page uses the correct theme.
```

## Code

```php
  function testBatchProgressPageTheme() {
    // Make sure that the page which starts the batch (an administrative page)
    // is using a different theme than would normally be used by the batch API.
    variable_set('theme_default', 'bartik');
    variable_set('admin_theme', 'seven');
    // Log in as an administrator who can see the administrative theme.
    $admin_user = $this->drupalCreateUser(array('view the administration theme'));
    $this->drupalLogin($admin_user);
    // Visit an administrative page that runs a test batch, and check that the
    // theme that was used during batch execution (which the batch callback
    // function saved as a variable) matches the theme used on the
    // administrative page.
    $this->drupalGet('admin/batch-test/test-theme');
    // The stack should contain the name of the theme used on the progress
    // page.
    $this->assertEqual(batch_test_stack(), array('seven'), t('A progressive batch correctly uses the theme of the page that started the batch.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
