# modules/locale/locale.admin.inc

- **Source:** [local](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · 1437 lines
- **Module/theme:** locale

## File documentation

```text
@file
Administration functions for locale.module.
```

## Functions (derived index)

- [locale_languages_overview_form()](locale_languages_overview_form.md) — User interface for the language overview screen.
- [theme_locale_languages_overview_form()](theme_locale_languages_overview_form.md) — Returns HTML for the language overview form.
- [locale_languages_overview_form_submit()](locale_languages_overview_form_submit.md) — Process language overview form submissions, updating existing languages.
- [locale_languages_add_screen()](locale_languages_add_screen.md) — User interface for the language addition screen.
- [locale_languages_predefined_form()](locale_languages_predefined_form.md) — Predefined language setup form.
- [locale_languages_custom_form()](locale_languages_custom_form.md) — Custom language addition form.
- [locale_languages_edit_form()](locale_languages_edit_form.md) — Editing screen for a particular language.
- [_locale_languages_common_controls()](_locale_languages_common_controls.md) — Common elements of the language addition and editing form.
- [locale_languages_predefined_form_validate()](locale_languages_predefined_form_validate.md) — Validate the language addition form.
- [locale_languages_predefined_form_submit()](locale_languages_predefined_form_submit.md) — Process the language addition form submission.
- [locale_languages_edit_form_validate()](locale_languages_edit_form_validate.md) — Validate the language editing form. Reused for custom language addition too.
- [locale_languages_edit_form_submit()](locale_languages_edit_form_submit.md) — Process the language editing form submission.
- [locale_languages_delete_form()](locale_languages_delete_form.md) — User interface for the language deletion confirmation screen.
- [locale_languages_delete_form_submit()](locale_languages_delete_form_submit.md) — Process language deletion submissions.
- [locale_languages_configure_form()](locale_languages_configure_form.md) — Setting for language negotiation options
- [_locale_languages_configure_form_language_table()](_locale_languages_configure_form_language_table.md) — Helper function to build a language provider table.
- [theme_locale_languages_configure_form()](theme_locale_languages_configure_form.md) — Returns HTML for a language configuration form.
- [locale_languages_configure_form_submit()](locale_languages_configure_form_submit.md) — Submit handler for language negotiation settings.
- [locale_language_providers_url_form()](locale_language_providers_url_form.md) — The URL language provider configuration form.
- [locale_language_providers_session_form()](locale_language_providers_session_form.md) — The URL language provider configuration form.
- [locale_translate_overview_screen()](locale_translate_overview_screen.md) — Overview screen for translations.
- [locale_translate_seek_screen()](locale_translate_seek_screen.md) — String search screen.
- [locale_translation_filters()](locale_translation_filters.md) — List locale translation filters that can be applied.
- [locale_translation_filter_form()](locale_translation_filter_form.md) — Return form for locale translation filters.
- [locale_translation_filter_form_validate()](locale_translation_filter_form_validate.md) — Validate result from locale translation filter form.
- [locale_translation_filter_form_submit()](locale_translation_filter_form_submit.md) — Process result from locale translation filter form.
- [locale_translate_import_form()](locale_translate_import_form.md) — User interface for the translation import screen.
- [locale_translate_import_form_submit()](locale_translate_import_form_submit.md) — Process the locale import form submission.
- [locale_translate_export_screen()](locale_translate_export_screen.md) — User interface for the translation export screen.
- [locale_translate_export_po_form()](locale_translate_export_po_form.md) — Form to export PO files for the languages provided.
- [locale_translate_export_pot_form()](locale_translate_export_pot_form.md) — Translation template export form.
- [locale_translate_export_po_form_submit()](locale_translate_export_po_form_submit.md) — Process a translation (or template) export form submission.
- [locale_translate_edit_form()](locale_translate_edit_form.md) — User interface for string editing.
- [locale_translate_edit_form_validate()](locale_translate_edit_form_validate.md) — Validate string editing form submissions.
- [locale_translate_edit_form_submit()](locale_translate_edit_form_submit.md) — Process string editing form submissions.
- [locale_translate_delete_page()](locale_translate_delete_page.md) — String deletion confirmation page.
- [locale_translate_delete_form()](locale_translate_delete_form.md) — User interface for the string deletion confirmation screen.
- [locale_translate_delete_form_submit()](locale_translate_delete_form_submit.md) — Process string deletion submissions.
- [theme_locale_date_format_form()](theme_locale_date_format_form.md) — Returns HTML for a locale date format form.
- [locale_date_format_language_overview_page()](locale_date_format_language_overview_page.md) — Display edit date format links for each language.
- [locale_date_format_form()](locale_date_format_form.md) — Provide date localization configuration options to users.
- [locale_date_format_form_submit()](locale_date_format_form_submit.md) — Submit handler for configuring localized date formats on the locale_date_format_form.
- [locale_date_format_reset_form()](locale_date_format_reset_form.md) — Reset locale specific date formats to the global defaults.
- [locale_date_format_reset_form_submit()](locale_date_format_reset_form_submit.md) — Reset date formats for a specific language to global defaults.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
