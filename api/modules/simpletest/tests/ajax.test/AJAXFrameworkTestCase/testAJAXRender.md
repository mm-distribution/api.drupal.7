# AJAXFrameworkTestCase::testAJAXRender()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 78–94 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L78-L94)
- **Class:** [AJAXFrameworkTestCase](../AJAXFrameworkTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAJAXRender()
```

## Documentation

```text
Test that ajax_render() returns JavaScript settings generated during the page request.

@todo Add tests to ensure that ajax_render() returns commands for new CSS
  and JavaScript files to be loaded by the page. See
  http://drupal.org/node/561858.
```

## Code

```php
  function testAJAXRender() {
    $commands = $this->drupalGetAJAX('ajax-test/render');

    // Verify that there is a command to load settings added with
    // drupal_add_js().
    $expected = array(
      'command' => 'settings',
      'settings' => array('basePath' => base_path(), 'ajax' => 'test'),
    );
    $this->assertCommand($commands, $expected, t('ajax_render() loads settings added with drupal_add_js().'));

    // Verify that Ajax settings are loaded for #type 'link'.
    $this->drupalGet('ajax-test/link');
    $settings = $this->drupalGetSettings();
    $this->assertEqual($settings['ajax']['ajax-link']['url'], url('filter/tips'));
    $this->assertEqual($settings['ajax']['ajax-link']['wrapper'], 'block-system-main');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
