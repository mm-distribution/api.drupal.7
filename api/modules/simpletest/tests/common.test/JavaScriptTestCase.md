# JavaScriptTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 1521–2061 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1521-L2061)
- **Module/theme:** batch_test

## Signature

```php
class JavaScriptTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests for the JavaScript system.
```

## Properties

### $preprocess_js

```php
protected $preprocess_js = NULL;
```

```text
Store configured value for JavaScript preprocessing.
```

## Methods (derived index)

- [getInfo()](JavaScriptTestCase/getInfo.md)
- [setUp()](JavaScriptTestCase/setUp.md)
- [tearDown()](JavaScriptTestCase/tearDown.md)
- [testDefault()](JavaScriptTestCase/testDefault.md) — Test default JavaScript is empty.
- [testAddFile()](JavaScriptTestCase/testAddFile.md) — Test adding a JavaScript file.
- [testAddSetting()](JavaScriptTestCase/testAddSetting.md) — Test adding settings.
- [testAddExternal()](JavaScriptTestCase/testAddExternal.md) — Tests adding an external JavaScript File.
- [testHeaderSetting()](JavaScriptTestCase/testHeaderSetting.md) — Test drupal_get_js() for JavaScript settings.
- [testReset()](JavaScriptTestCase/testReset.md) — Test to see if resetting the JavaScript empties the cache.
- [testAddInline()](JavaScriptTestCase/testAddInline.md) — Test adding inline scripts.
- [testRenderExternal()](JavaScriptTestCase/testRenderExternal.md) — Test rendering an external JavaScript file.
- [testFooterHTML()](JavaScriptTestCase/testFooterHTML.md) — Test drupal_get_js() with a footer scope.
- [testJavaScriptAlwaysUseJQuery()](JavaScriptTestCase/testJavaScriptAlwaysUseJQuery.md) — Test the 'javascript_always_use_jquery' variable.
- [testDoubleSubmitFormProtection()](JavaScriptTestCase/testDoubleSubmitFormProtection.md) — Tests the double submit form protection and 'javascript_use_double_submit_protection' variable.
- [testNoCache()](JavaScriptTestCase/testNoCache.md) — Test drupal_add_js() sets preproccess to false when cache is set to false.
- [testDifferentGroup()](JavaScriptTestCase/testDifferentGroup.md) — Test adding a JavaScript file with a different group.
- [testDifferentWeight()](JavaScriptTestCase/testDifferentWeight.md) — Test adding a JavaScript file with a different weight.
- [testAggregationOrder()](JavaScriptTestCase/testAggregationOrder.md) — Tests JavaScript aggregation when files are added to a different scope.
- [testRenderOrder()](JavaScriptTestCase/testRenderOrder.md) — Test JavaScript ordering.
- [testRenderDifferentWeight()](JavaScriptTestCase/testRenderDifferentWeight.md) — Test rendering the JavaScript with a file's weight above jQuery's.
- [testAlter()](JavaScriptTestCase/testAlter.md) — Test altering a JavaScript's weight via hook_js_alter().
- [testLibraryRender()](JavaScriptTestCase/testLibraryRender.md) — Adds a library to the page and tests for both its JavaScript and its CSS.
- [testLibraryAlter()](JavaScriptTestCase/testLibraryAlter.md) — Adds a JavaScript library to the page and alters it.
- [testLibraryNameConflicts()](JavaScriptTestCase/testLibraryNameConflicts.md) — Tests that multiple modules can implement the same library.
- [testLibraryUnknown()](JavaScriptTestCase/testLibraryUnknown.md) — Tests non-existing libraries.
- [testAttachedLibrary()](JavaScriptTestCase/testAttachedLibrary.md) — Tests the addition of libraries through the #attached['library'] property.
- [testGetLibrary()](JavaScriptTestCase/testGetLibrary.md) — Tests retrieval of libraries via drupal_get_library().
- [testAddJsFileWithQueryString()](JavaScriptTestCase/testAddJsFileWithQueryString.md) — Tests that the query string remains intact when adding JavaScript files that have query string parameters.
- [testSetHasJsCookie()](JavaScriptTestCase/testSetHasJsCookie.md) — Tests that the set_has_js_cookie variable is reflected in Drupal.settings.
- [resetStaticVariables()](JavaScriptTestCase/resetStaticVariables.md) — Resets static variables related to adding JavaScript to a page.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
