# AJAXFrameworkTestCase::testAJAXRenderError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 99–118 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L99-L118)
- **Class:** [AJAXFrameworkTestCase](../AJAXFrameworkTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAJAXRenderError()
```

## Documentation

```text
Test behavior of ajax_render_error().
```

## Code

```php
  function testAJAXRenderError() {
    // Verify default error message.
    $commands = $this->drupalGetAJAX('ajax-test/render-error');
    $expected = array(
      'command' => 'alert',
      'text' => t('An error occurred while handling the request: The server received invalid input.'),
    );
    $this->assertCommand($commands, $expected, t('ajax_render_error() invokes alert command.'));

    // Verify custom error message.
    $edit = array(
      'message' => 'Custom error message.',
    );
    $commands = $this->drupalGetAJAX('ajax-test/render-error', array('query' => $edit));
    $expected = array(
      'command' => 'alert',
      'text' => $edit['message'],
    );
     $this->assertCommand($commands, $expected, t('Custom error message is output.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
