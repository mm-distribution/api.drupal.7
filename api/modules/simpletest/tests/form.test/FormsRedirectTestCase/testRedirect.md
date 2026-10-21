# FormsRedirectTestCase::testRedirect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1837–1888 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1837-L1888)
- **Class:** [FormsRedirectTestCase](../FormsRedirectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRedirect()
```

## Documentation

```text
Tests form redirection.
```

## Code

```php
  function testRedirect() {
    $path = 'form-test/redirect';
    $options = array('query' => array('foo' => 'bar'));
    $options['absolute'] = TRUE;

    // Test basic redirection.
    $edit = array(
      'redirection' => TRUE,
      'destination' => $this->randomName(),
    );
    $this->drupalPost($path, $edit, t('Submit'));
    $this->assertUrl($edit['destination'], array(), 'Basic redirection works.');


    // Test without redirection.
    $edit = array(
      'redirection' => FALSE,
    );
    $this->drupalPost($path, $edit, t('Submit'));
    $this->assertUrl($path, array(), 'When redirect is set to FALSE, there should be no redirection.');

    // Test redirection with query parameters.
    $edit = array(
      'redirection' => TRUE,
      'destination' => $this->randomName(),
    );
    $this->drupalPost($path, $edit, t('Submit'), $options);
    $this->assertUrl($edit['destination'], array(), 'Redirection with query parameters works.');

    // Test without redirection but with query parameters.
    $edit = array(
      'redirection' => FALSE,
    );
    $this->drupalPost($path, $edit, t('Submit'), $options);
    $this->assertUrl($path, $options, 'When redirect is set to FALSE, there should be no redirection, and the query parameters should be passed along.');

    // Test redirection back to the original path.
    $edit = array(
      'redirection' => TRUE,
      'destination' => '',
    );
    $this->drupalPost($path, $edit, t('Submit'));
    $this->assertUrl($path, array(), 'When using an empty redirection string, there should be no redirection.');

    // Test redirection back to the original path with query parameters.
    $edit = array(
      'redirection' => TRUE,
      'destination' => '',
    );
    $this->drupalPost($path, $edit, t('Submit'), $options);
    $this->assertUrl($path, $options, 'When using an empty redirection string, there should be no redirection, and the query parameters should be passed along.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
