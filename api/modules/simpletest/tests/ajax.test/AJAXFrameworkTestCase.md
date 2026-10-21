# AJAXFrameworkTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/ajax.test`](_file.md), lines 60–219 · [local source](../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L60-L219)
- **Module/theme:** batch_test

## Signature

```php
class AJAXFrameworkTestCase extends AJAXTestCase
```

## Documentation

```text
Tests primary Ajax framework functions.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [getInfo()](AJAXFrameworkTestCase/getInfo.md)
- [testAJAXRender()](AJAXFrameworkTestCase/testAJAXRender.md) — Test that ajax_render() returns JavaScript settings generated during the page request.
- [testAJAXRenderError()](AJAXFrameworkTestCase/testAJAXRenderError.md) — Test behavior of ajax_render_error().
- [testLazyLoad()](AJAXFrameworkTestCase/testLazyLoad.md) — Test that new JavaScript and CSS files added during an AJAX request are returned.
- [testLazyLoadOverriddenCSS()](AJAXFrameworkTestCase/testLazyLoadOverriddenCSS.md) — Tests that overridden CSS files are not added during lazy load.

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
