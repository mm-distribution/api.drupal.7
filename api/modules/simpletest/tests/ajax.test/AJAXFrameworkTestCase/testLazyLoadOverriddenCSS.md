# AJAXFrameworkTestCase::testLazyLoadOverriddenCSS()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 202–218 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L202-L218)
- **Class:** [AJAXFrameworkTestCase](../AJAXFrameworkTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLazyLoadOverriddenCSS()
```

## Documentation

```text
Tests that overridden CSS files are not added during lazy load.
```

## Code

```php
  function testLazyLoadOverriddenCSS() {
    // The test theme overrides system.base.css without an implementation,
    // thereby removing it.
    theme_enable(array('test_theme'));
    variable_set('theme_default', 'test_theme');

    // This gets the form, and emulates an Ajax submission on it, including
    // adding markup to the HEAD and BODY for any lazy loaded JS/CSS files.
    $this->drupalPostAJAX('ajax_forms_test_lazy_load_form', array('add_files' => TRUE), array('op' => t('Submit')));

    // Verify that the resulting HTML does not load the overridden CSS file.
    // We add a "?" to the assertion, because Drupal.settings may include
    // information about the file; we only really care about whether it appears
    // in a LINK or STYLE tag, for which Drupal always adds a query string for
    // cache control.
    $this->assertNoText('system.base.css?', 'Ajax lazy loading does not add overridden CSS files.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
