# modules/poll/poll.module

- **Source:** [local](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · 1012 lines
- **Module/theme:** poll

## File documentation

```text
@file
Enables your site to capture votes on different topics in the form of multiple
choice questions.
```

## Functions (derived index)

- [poll_help()](poll_help.md) — Implements hook_help().
- [poll_theme()](poll_theme.md) — Implements hook_theme().
- [poll_permission()](poll_permission.md) — Implements hook_permission().
- [poll_menu()](poll_menu.md) — Implements hook_menu().
- [_poll_menu_access()](_poll_menu_access.md) — Callback function to see if a node is acceptable for poll menu items.
- [poll_block_info()](poll_block_info.md) — Implements hook_block_info().
- [poll_block_view()](poll_block_view.md) — Implements hook_block_view().
- [poll_cron()](poll_cron.md) — Implements hook_cron().
- [poll_node_info()](poll_node_info.md) — Implements hook_node_info().
- [poll_field_extra_fields()](poll_field_extra_fields.md) — Implements hook_field_extra_fields().
- [poll_form()](poll_form.md) — Implements hook_form().
- [poll_more_choices_submit()](poll_more_choices_submit.md) — Submit handler to add more choices to a poll form.
- [_poll_choice_form()](_poll_choice_form.md)
- [poll_choice_js()](poll_choice_js.md) — Ajax callback in response to new choices being added to the form.
- [poll_node_form_submit()](poll_node_form_submit.md) — Form submit handler for node_form().
- [poll_validate()](poll_validate.md) — Implements hook_validate().
- [poll_field_attach_prepare_translation_alter()](poll_field_attach_prepare_translation_alter.md) — Implements hook_field_attach_prepare_translation_alter().
- [poll_load()](poll_load.md) — Implements hook_load().
- [poll_insert()](poll_insert.md) — Implements hook_insert().
- [poll_update()](poll_update.md) — Implements hook_update().
- [poll_delete()](poll_delete.md) — Implements hook_delete().
- [poll_block_latest_poll_view()](poll_block_latest_poll_view.md) — Return content for 'latest poll' block.
- [poll_view()](poll_view.md) — Implements hook_view().
- [poll_teaser()](poll_teaser.md) — Creates a simple teaser that lists all the choices.
- [poll_view_voting()](poll_view_voting.md) — Generates the voting form for a poll.
- [poll_view_voting_validate()](poll_view_voting_validate.md) — Validation function for processing votes
- [poll_vote()](poll_vote.md) — Submit handler for processing a vote.
- [template_preprocess_poll_vote()](template_preprocess_poll_vote.md) — Themes the voting form for a poll.
- [poll_view_results()](poll_view_results.md) — Generates a graphical representation of the results of a poll.
- [theme_poll_choices()](theme_poll_choices.md) — Returns HTML for an admin poll form for choices.
- [template_preprocess_poll_results()](template_preprocess_poll_results.md) — Preprocess the poll_results theme hook.
- [template_preprocess_poll_bar()](template_preprocess_poll_bar.md) — Preprocess the poll_bar theme hook.
- [poll_cancel_form()](poll_cancel_form.md) — Builds the cancel form for a poll.
- [poll_cancel()](poll_cancel.md) — Submit callback for poll_cancel_form().
- [poll_user_cancel()](poll_user_cancel.md) — Implements hook_user_cancel().
- [poll_user_delete()](poll_user_delete.md) — Implements hook_user_delete().
- [poll_rdf_mapping()](poll_rdf_mapping.md) — Implements hook_rdf_mapping().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
