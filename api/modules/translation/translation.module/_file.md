# modules/translation/translation.module

- **Source:** [local](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · 577 lines
- **Module/theme:** translation

## File documentation

```text
@file
Manages content translations.

Translations are managed in sets of posts, which represent the same
information in different languages. Only content types for which the
administrator has explicitly enabled translations could have translations
associated. Translations are managed in sets with exactly one source post
per set. The source post is used to translate to different languages, so if
the source post is significantly updated, the editor can decide to mark all
translations outdated.

The node table stores the values used by this module:
- tnid: Integer for the translation set ID, which equals the node ID of the
  source post.
- translate: Integer flag, either indicating that the translation is up to
  date (0) or needs to be updated (1).
```

## Functions (derived index)

- [translation_help()](translation_help.md) — Implements hook_help().
- [translation_menu()](translation_menu.md) — Implements hook_menu().
- [_translation_tab_access()](_translation_tab_access.md) — Access callback: Checks that the user has permission to 'translate content'.
- [translation_admin_paths()](translation_admin_paths.md) — Implements hook_admin_paths().
- [translation_permission()](translation_permission.md) — Implements hook_permission().
- [translation_form_node_type_form_alter()](translation_form_node_type_form_alter.md) — Implements hook_form_FORM_ID_alter() for node_type_form().
- [translation_form_node_form_alter()](translation_form_node_form_alter.md) — Implements hook_form_BASE_FORM_ID_alter() for node_form().
- [translation_node_view()](translation_node_view.md) — Implements hook_node_view().
- [translation_node_prepare()](translation_node_prepare.md) — Implements hook_node_prepare().
- [translation_node_insert()](translation_node_insert.md) — Implements hook_node_insert().
- [translation_node_update()](translation_node_update.md) — Implements hook_node_update().
- [translation_node_validate()](translation_node_validate.md) — Implements hook_node_validate().
- [translation_node_delete()](translation_node_delete.md) — Implements hook_node_delete().
- [translation_remove_from_set()](translation_remove_from_set.md) — Removes a node from its translation set and updates accordingly.
- [translation_node_get_translations()](translation_node_get_translations.md) — Gets all nodes in a given translation set.
- [translation_supported_type()](translation_supported_type.md) — Returns whether the given content type has support for translations.
- [translation_path_get_translations()](translation_path_get_translations.md) — Returns the paths of all translations of a node, based on its Drupal path.
- [translation_language_switch_links_alter()](translation_language_switch_links_alter.md) — Implements hook_language_switch_links_alter().

## Constants

### TRANSLATION_ENABLED

- Line 25

```php
define('TRANSLATION_ENABLED', 2);
```

```text
Identifies a content type which has translation support enabled.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
