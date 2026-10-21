# modules/menu/menu.admin.inc

- **Source:** [local](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · 721 lines
- **Module/theme:** menu

## File documentation

```text
@file
Administrative page callbacks for menu module.
```

## Functions (derived index)

- [menu_overview_page()](menu_overview_page.md) — Menu callback which shows an overview page of all the custom menus and their descriptions.
- [theme_menu_admin_overview()](theme_menu_admin_overview.md) — Returns HTML for a menu title and description for the menu overview page.
- [menu_overview_form()](menu_overview_form.md) — Form for editing an entire menu tree at once.
- [_menu_overview_tree_form()](_menu_overview_tree_form.md) — Recursive helper function for menu_overview_form().
- [menu_overview_form_submit()](menu_overview_form_submit.md) — Submit handler for the menu overview form.
- [theme_menu_overview_form()](theme_menu_overview_form.md) — Returns HTML for the menu overview form into a table.
- [menu_edit_item()](menu_edit_item.md) — Menu callback; Build the menu link editing form.
- [menu_edit_item_validate()](menu_edit_item_validate.md) — Validate form values for a menu link being added or edited.
- [menu_item_delete_submit()](menu_item_delete_submit.md) — Submit function for the delete button on the menu item editing form.
- [menu_edit_item_submit()](menu_edit_item_submit.md) — Process menu and menu item add/edit form submissions.
- [menu_edit_menu()](menu_edit_menu.md) — Menu callback; Build the form that handles the adding/editing of a custom menu.
- [menu_custom_delete_submit()](menu_custom_delete_submit.md) — Submit function for the 'Delete' button on the menu editing form.
- [menu_delete_menu_page()](menu_delete_menu_page.md) — Menu callback; check access and get a confirm form for deletion of a custom menu.
- [menu_delete_menu_confirm()](menu_delete_menu_confirm.md) — Build a confirm form for deletion of a custom menu.
- [menu_delete_menu_confirm_submit()](menu_delete_menu_confirm_submit.md) — Delete a custom menu and all links in it.
- [menu_edit_menu_name_exists()](menu_edit_menu_name_exists.md) — Returns whether a menu name already exists.
- [menu_edit_menu_submit()](menu_edit_menu_submit.md) — Submit function for adding or editing a custom menu.
- [menu_item_delete_page()](menu_item_delete_page.md) — Menu callback; Check access and present a confirm form for deleting a menu link.
- [menu_item_delete_form()](menu_item_delete_form.md) — Build a confirm form for deletion of a single menu link.
- [menu_item_delete_form_submit()](menu_item_delete_form_submit.md) — Process menu delete form submissions.
- [menu_reset_item_confirm()](menu_reset_item_confirm.md) — Menu callback; reset a single modified menu link.
- [menu_reset_item_confirm_submit()](menu_reset_item_confirm_submit.md) — Process menu reset item form submissions.
- [menu_configure()](menu_configure.md) — Menu callback; Build the form presenting menu configuration options.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
