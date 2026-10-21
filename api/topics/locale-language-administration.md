# Language administration interface

- **Topic id:** `locale-language-administration`
- **Defined in:** [`modules/locale/locale.admin.inc`](../modules/locale/locale.admin.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L8)

## Documentation

```text
@defgroup locale-language-administration Language administration interface
@{
Administration interface for languages.

These functions provide the user interface to show, add, edit and
delete languages as well as providing options for language negotiation.
```

## Members (derived, 20)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_locale_languages_common_controls()](../modules/locale/locale.admin.inc/_locale_languages_common_controls.md) (function) — Common elements of the language addition and editing form.
- [_locale_languages_configure_form_language_table()](../modules/locale/locale.admin.inc/_locale_languages_configure_form_language_table.md) (function) — Helper function to build a language provider table.
- [locale_language_providers_session_form()](../modules/locale/locale.admin.inc/locale_language_providers_session_form.md) (function) — The URL language provider configuration form.
- [locale_language_providers_url_form()](../modules/locale/locale.admin.inc/locale_language_providers_url_form.md) (function) — The URL language provider configuration form.
- [locale_languages_add_screen()](../modules/locale/locale.admin.inc/locale_languages_add_screen.md) (function) — User interface for the language addition screen.
- [locale_languages_configure_form()](../modules/locale/locale.admin.inc/locale_languages_configure_form.md) (function) — Setting for language negotiation options
- [locale_languages_configure_form_submit()](../modules/locale/locale.admin.inc/locale_languages_configure_form_submit.md) (function) — Submit handler for language negotiation settings.
- [locale_languages_custom_form()](../modules/locale/locale.admin.inc/locale_languages_custom_form.md) (function) — Custom language addition form.
- [locale_languages_delete_form()](../modules/locale/locale.admin.inc/locale_languages_delete_form.md) (function) — User interface for the language deletion confirmation screen.
- [locale_languages_delete_form_submit()](../modules/locale/locale.admin.inc/locale_languages_delete_form_submit.md) (function) — Process language deletion submissions.
- [locale_languages_edit_form()](../modules/locale/locale.admin.inc/locale_languages_edit_form.md) (function) — Editing screen for a particular language.
- [locale_languages_edit_form_submit()](../modules/locale/locale.admin.inc/locale_languages_edit_form_submit.md) (function) — Process the language editing form submission.
- [locale_languages_edit_form_validate()](../modules/locale/locale.admin.inc/locale_languages_edit_form_validate.md) (function) — Validate the language editing form. Reused for custom language addition too.
- [locale_languages_overview_form()](../modules/locale/locale.admin.inc/locale_languages_overview_form.md) (function) — User interface for the language overview screen.
- [locale_languages_overview_form_submit()](../modules/locale/locale.admin.inc/locale_languages_overview_form_submit.md) (function) — Process language overview form submissions, updating existing languages.
- [locale_languages_predefined_form()](../modules/locale/locale.admin.inc/locale_languages_predefined_form.md) (function) — Predefined language setup form.
- [locale_languages_predefined_form_submit()](../modules/locale/locale.admin.inc/locale_languages_predefined_form_submit.md) (function) — Process the language addition form submission.
- [locale_languages_predefined_form_validate()](../modules/locale/locale.admin.inc/locale_languages_predefined_form_validate.md) (function) — Validate the language addition form.
- [theme_locale_languages_configure_form()](../modules/locale/locale.admin.inc/theme_locale_languages_configure_form.md) (function) — Returns HTML for a language configuration form.
- [theme_locale_languages_overview_form()](../modules/locale/locale.admin.inc/theme_locale_languages_overview_form.md) (function) — Returns HTML for the language overview form.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
