# modules/locale/locale.test

- **Source:** [local](../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · 3331 lines
- **Module/theme:** locale

## File documentation

```text
@file
Tests for locale.module.

The test file includes:
 - a functional test for the language configuration forms;
 - functional tests for the translation functionalities, including searching;
 - a functional test for the PO files import feature, including validation;
 - functional tests for translations and templates export feature;
 - functional tests for the uninstall process;
 - a functional test for the language switching feature;
 - a functional test for a user's ability to change their default language;
 - a functional test for configuring a different path alias per language;
 - a functional test for configuring a different path alias per language;
 - a functional test for multilingual support by content type and on nodes.
 - a functional test for multilingual fields.
 - a functional test for comment language.
 - a functional test fot language types/negotiation info.
```

## Classes and interfaces (derived index)

- [LocaleConfigurationTest](LocaleConfigurationTest.md) — Functional tests for the language configuration forms.
- [LocaleLibraryInfoAlterTest](LocaleLibraryInfoAlterTest.md) — Tests localization of the JavaScript libraries.
- [LocaleJavascriptTranslationTest](LocaleJavascriptTranslationTest.md) — Functional tests for JavaScript parsing for translatable strings.
- [LocaleTranslationFunctionalTest](LocaleTranslationFunctionalTest.md) — Functional test for string translation and validation.
- [LocalePluralFormatTest](LocalePluralFormatTest.md) — Tests plural index computation functionality.
- [LocaleImportFunctionalTest](LocaleImportFunctionalTest.md) — Functional tests for the import of translation files.
- [LocaleExportFunctionalTest](LocaleExportFunctionalTest.md) — Functional tests for the export of translation files.
- [LocaleInstallTest](LocaleInstallTest.md) — Tests for the st() function.
- [LocaleUninstallFunctionalTest](LocaleUninstallFunctionalTest.md) — Locale uninstall with English UI functional test.
- [LocaleUninstallFrenchFunctionalTest](LocaleUninstallFrenchFunctionalTest.md) — Locale uninstall with French UI functional test.
- [LocaleLanguageSwitchingFunctionalTest](LocaleLanguageSwitchingFunctionalTest.md) — Functional tests for the language switching feature.
- [LocaleBrowserDetectionTest](LocaleBrowserDetectionTest.md) — Test browser language detection.
- [LocaleUserLanguageFunctionalTest](LocaleUserLanguageFunctionalTest.md) — Functional tests for a user's ability to change their default language.
- [LocaleUserCreationTest](LocaleUserCreationTest.md) — Functional test for language handling during user creation.
- [LocalePathFunctionalTest](LocalePathFunctionalTest.md) — Functional tests for configuring a different path alias per language.
- [LocaleContentFunctionalTest](LocaleContentFunctionalTest.md) — Functional tests for multilingual support on nodes.
- [LocaleUILanguageNegotiationTest](LocaleUILanguageNegotiationTest.md) — Test UI language negotiation 1. URL (PATH) > DEFAULT UI Language base on URL prefix, browser language preference has no influence: admin/config UI in site default language zh-hans/admin/config UI in Chinese blah-blah/admin/config 404 2. URL (PATH) > BROWSER > DEFAULT admin/config UI in user's browser language preference if the site has that language enabled, if not, the default language zh-hans/admin/config UI in Chinese blah-blah/admin/config 404 3. URL (DOMAIN) > DEFAULT http://example.com/admin/config UI language in site default http://example.cn/admin/config UI language in Chinese
- [LocaleUrlRewritingTest](LocaleUrlRewritingTest.md) — Test that URL rewriting works as expected.
- [LocaleMultilingualFieldsFunctionalTest](LocaleMultilingualFieldsFunctionalTest.md) — Functional test for multilingual fields.
- [LocaleCommentLanguageFunctionalTest](LocaleCommentLanguageFunctionalTest.md) — Functional tests for comment language.
- [LocaleDateFormatsFunctionalTest](LocaleDateFormatsFunctionalTest.md) — Functional tests for localizing date formats.
- [LocaleLanguageNegotiationInfoFunctionalTest](LocaleLanguageNegotiationInfoFunctionalTest.md) — Functional test for language types/negotiation info.
- [LocaleCSSAlterTest](LocaleCSSAlterTest.md) — Functional tests for CSS alter functions.
- [LocaleStringIsSafeTest](LocaleStringIsSafeTest.md) — Tests locale translation safe string handling.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
