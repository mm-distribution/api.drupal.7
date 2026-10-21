# poll_update_7001()

- **Type:** Function
- **File:** [`modules/poll/poll.install`](_file.md), lines 157–174 · [local source](../../../../source/modules/poll/poll.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install#L157-L174)
- **Module/theme:** poll

## Signature

```php
function poll_update_7001()
```

## Documentation

```text
Use the poll_choice primary key to record votes in poll_votes rather than
the choice order. Rename chorder to weight.

Rename {poll_choices} table to {poll_choice} and {poll_votes} to {poll_vote}.
```

## Code

```php
function poll_update_7001() {
  // Add chid column and convert existing votes.
  db_add_field('poll_votes', 'chid', array('type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE, 'default' => 0));
  db_add_index('poll_votes', 'chid', array('chid'));
  db_update('poll_votes')
    ->expression('chid', Database::getConnection()->prefixTables('COALESCE((SELECT chid FROM {poll_choices} c WHERE {poll_votes}.chorder = c.chorder AND {poll_votes}.nid = c.nid), 0)'))
    ->execute();
  // Delete invalid votes.
  db_delete('poll_votes')->condition('chid', 0)->execute();
  // Remove old chorder column.
  db_drop_field('poll_votes', 'chorder');

  // Change the chorder column to weight in poll_choices.
  db_change_field('poll_choices', 'chorder', 'weight', array('type' => 'int', 'not null' => TRUE, 'default' => 0, 'size' => 'tiny'));

  db_rename_table('poll_votes', 'poll_vote');
  db_rename_table('poll_choices', 'poll_choice');
}
```

---
_Drupal 7.103 · [modules/poll/poll.install](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install) · Licensed GPL-2.0-or-later (see LICENSE)._
