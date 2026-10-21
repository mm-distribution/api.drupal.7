# modules/locale/locale.module

- **Source:** [local](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · 1102 lines
- **Module/theme:** locale

## File documentation

```text
@file
  Add language handling functionality and enables the translation of the
  user interface to languages other than English.

  When enabled, multiple languages can be set up. The site interface
  can be displayed in different languages, as well as nodes can have languages
  assigned. The setup of languages and translations is completely web based.
  Gettext portable object files are supported.
```

## Functions (derived index)

- [locale_help()](locale_help.md) — Implements hook_help().
- [locale_menu()](locale_menu.md) — Implements hook_menu().
- [locale_init()](locale_init.md) — Implements hook_init().
- [locale_permission()](locale_permission.md) — Implements hook_permission().
- [locale_locale()](locale_locale.md) — Implements hook_locale().
- [locale_language_selector_form()](locale_language_selector_form.md) — Form builder callback to display language selection widget.
- [locale_form_path_admin_form_alter()](locale_form_path_admin_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [locale_form_node_type_form_alter()](locale_form_node_type_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [locale_multilingual_node_type()](locale_multilingual_node_type.md) — Return whether the given content type has multilingual support.
- [locale_form_alter()](locale_form_alter.md) — Implements hook_form_alter().
- [locale_form_node_form_alter()](locale_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter().
- [locale_field_node_form_submit()](locale_field_node_form_submit.md) — Form submit handler for node_form().
- [locale_form_comment_form_alter()](locale_form_comment_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [locale_field_comment_form_submit()](locale_field_comment_form_submit.md) — Form submit handler for comment_form().
- [locale_field_entity_form_submit()](locale_field_entity_form_submit.md) — Handles field language on submit for the given entity type.
- [locale_theme()](locale_theme.md) — Implements hook_theme().
- [locale_field_language_alter()](locale_field_language_alter.md) — Implements hook_field_language_alter().
- [locale_field_language_fallback()](locale_field_language_fallback.md) — Applies language fallback rules to the fields attached to the given entity.
- [locale_entity_info_alter()](locale_entity_info_alter.md) — Implements hook_entity_info_alter().
- [locale_language_types_info()](locale_language_types_info.md) — Implements hook_language_types_info().
- [locale_language_negotiation_info()](locale_language_negotiation_info.md) — Implements hook_language_negotiation_info().
- [locale_modules_enabled()](locale_modules_enabled.md) — Implements hook_modules_enabled().
- [locale_modules_disabled()](locale_modules_disabled.md) — Implements hook_modules_disabled().
- [locale()](locale.md) — Provides interface translation services.
- [locale_reset()](locale_reset.md) — Reset static variables used by locale().
- [locale_get_plural()](locale_get_plural.md) — Returns plural form index for a specific number.
- [locale_language_name()](locale_language_name.md) — Returns a language name
- [locale_language_list()](locale_language_list.md) — Returns array of language names
- [locale_modules_installed()](locale_modules_installed.md) — Implements hook_modules_installed().
- [locale_themes_enabled()](locale_themes_enabled.md) — Implements hook_themes_enabled().
- [locale_system_update()](locale_system_update.md) — Imports translations when new modules or themes are installed.
- [locale_js_alter()](locale_js_alter.md) — Implements hook_js_alter().
- [locale_css_alter()](locale_css_alter.md) — Implements hook_css_alter().
- [locale_library_alter()](locale_library_alter.md) — Implement hook_library_alter().
- [locale_block_info()](locale_block_info.md) — Implements hook_block_info().
- [locale_block_view()](locale_block_view.md) — Implements hook_block_view().
- [locale_url_outbound_alter()](locale_url_outbound_alter.md) — Implements hook_url_outbound_alter().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
