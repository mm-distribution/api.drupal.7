# CascadingStylesheetsTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 748–1004 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L748-L1004)
- **Module/theme:** batch_test

## Signature

```php
class CascadingStylesheetsTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test the Drupal CSS system.
```

## Methods (derived index)

- [getInfo()](CascadingStylesheetsTestCase/getInfo.md)
- [setUp()](CascadingStylesheetsTestCase/setUp.md)
- [testDefault()](CascadingStylesheetsTestCase/testDefault.md) — Check default stylesheets as empty.
- [testModuleInfo()](CascadingStylesheetsTestCase/testModuleInfo.md) — Test that stylesheets in module .info files are loaded.
- [testAddFile()](CascadingStylesheetsTestCase/testAddFile.md) — Tests adding a file stylesheet.
- [testAddExternal()](CascadingStylesheetsTestCase/testAddExternal.md) — Tests adding an external stylesheet.
- [testReset()](CascadingStylesheetsTestCase/testReset.md) — Makes sure that reseting the CSS empties the cache.
- [testRenderFile()](CascadingStylesheetsTestCase/testRenderFile.md) — Tests rendering the stylesheets.
- [testRenderExternal()](CascadingStylesheetsTestCase/testRenderExternal.md) — Tests rendering an external stylesheet.
- [testRenderInlinePreprocess()](CascadingStylesheetsTestCase/testRenderInlinePreprocess.md) — Tests rendering inline stylesheets with preprocessing on.
- [testRenderRemoveCharsetPreprocess()](CascadingStylesheetsTestCase/testRenderRemoveCharsetPreprocess.md) — Tests removing charset when rendering stylesheets with preprocessing on.
- [testRenderInlineNoPreprocess()](CascadingStylesheetsTestCase/testRenderInlineNoPreprocess.md) — Tests rendering inline stylesheets with preprocessing off.
- [testRenderInlineFullPage()](CascadingStylesheetsTestCase/testRenderInlineFullPage.md) — Tests rendering inline stylesheets through a full page request.
- [testRenderOrder()](CascadingStylesheetsTestCase/testRenderOrder.md) — Test CSS ordering.
- [testRenderOverride()](CascadingStylesheetsTestCase/testRenderOverride.md) — Test CSS override.
- [testAlter()](CascadingStylesheetsTestCase/testAlter.md) — Tests Locale module's CSS Alter to include RTL overrides.
- [testAddCssFileWithQueryString()](CascadingStylesheetsTestCase/testAddCssFileWithQueryString.md) — Tests that the query string remains intact when adding CSS files that have query string parameters.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
