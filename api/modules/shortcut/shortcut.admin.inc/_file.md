# modules/shortcut/shortcut.admin.inc

- **Source:** [local](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · 789 lines
- **Module/theme:** shortcut

## File documentation

```text
@file
Administrative page callbacks for the shortcut module.
```

## Functions (derived index)

- [shortcut_max_slots()](shortcut_max_slots.md) — Returns the maximum number of shortcut "slots" available per shortcut set.
- [shortcut_set_switch()](shortcut_set_switch.md) — Form callback: builds the form for switching shortcut sets.
- [shortcut_set_switch_validate()](shortcut_set_switch_validate.md) — Validation handler for shortcut_set_switch().
- [shortcut_set_switch_submit()](shortcut_set_switch_submit.md) — Submit handler for shortcut_set_switch().
- [shortcut_set_admin()](shortcut_set_admin.md) — Menu page callback: builds the page for administering shortcut sets.
- [shortcut_set_add_form()](shortcut_set_add_form.md) — Form callback: builds the form for adding a shortcut set.
- [shortcut_set_add_form_validate()](shortcut_set_add_form_validate.md) — Validation handler for shortcut_set_add_form().
- [shortcut_set_add_form_submit()](shortcut_set_add_form_submit.md) — Submit handler for shortcut_set_add_form().
- [shortcut_set_customize()](shortcut_set_customize.md) — Form callback: builds the form for customizing shortcut sets.
- [shortcut_set_customize_submit()](shortcut_set_customize_submit.md) — Submit handler for shortcut_set_customize().
- [theme_shortcut_set_customize()](theme_shortcut_set_customize.md) — Returns HTML for a shortcut set customization form.
- [shortcut_link_add()](shortcut_link_add.md) — Form callback: builds the form for adding a new shortcut link.
- [shortcut_link_edit()](shortcut_link_edit.md) — Form callback: builds the form for editing a shortcut link.
- [_shortcut_link_form_elements()](_shortcut_link_form_elements.md) — Helper function for building a form for adding or editing shortcut links.
- [shortcut_link_edit_validate()](shortcut_link_edit_validate.md) — Validation handler for the shortcut link add and edit forms.
- [shortcut_link_edit_submit()](shortcut_link_edit_submit.md) — Submit handler for shortcut_link_edit().
- [shortcut_link_add_submit()](shortcut_link_add_submit.md) — Submit handler for shortcut_link_add().
- [shortcut_admin_add_link()](shortcut_admin_add_link.md) — Adds a link to the end of a shortcut set, keeping within a prescribed limit.
- [shortcut_set_edit_form()](shortcut_set_edit_form.md) — Form callback: builds the form for editing the shortcut set name.
- [shortcut_set_edit_form_validate()](shortcut_set_edit_form_validate.md) — Validation handler for shortcut_set_edit_form().
- [shortcut_set_edit_form_submit()](shortcut_set_edit_form_submit.md) — Submit handler for shortcut_set_edit_form().
- [shortcut_set_delete_form()](shortcut_set_delete_form.md) — Form callback: builds the confirmation form for deleting a shortcut set.
- [shortcut_set_delete_form_submit()](shortcut_set_delete_form_submit.md) — Submit handler for shortcut_set_delete_form().
- [shortcut_link_delete()](shortcut_link_delete.md) — Form callback: builds the confirmation form for deleting a shortcut link.
- [shortcut_link_delete_submit()](shortcut_link_delete_submit.md) — Submit handler for shortcut_link_delete_submit().
- [shortcut_link_add_inline()](shortcut_link_add_inline.md) — Menu page callback: creates a new link in the provided shortcut set.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
