# poll_votes()

- **Type:** Function
- **File:** [`modules/poll/poll.pages.inc`](_file.md), lines 51–88 · [local source](../../../../source/modules/poll/poll.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.pages.inc#L51-L88)
- **Module/theme:** poll

## Signature

```php
function poll_votes($node)
```

## Documentation

```text
Callback for the 'votes' tab for polls you can see other votes on
```

## Code

```php
function poll_votes($node) {
  $votes_per_page = 20;
  drupal_set_title($node->title);

  $header[] = array('data' => t('Visitor'), 'field' => 'u.name');
  $header[] = array('data' => t('Vote'), 'field' => 'pc.chtext');
  $header[] = array('data' => t('Timestamp'), 'field' => 'pv.timestamp', 'sort' => 'desc');

  $select = db_select('poll_vote', 'pv')->extend('PagerDefault')->extend('TableSort');
  $select->join('poll_choice', 'pc', 'pv.chid = pc.chid');
  $select->join('users', 'u', 'pv.uid = u.uid');
  $queried_votes = $select
    ->addTag('translatable')
    ->fields('pv', array('chid', 'uid', 'hostname', 'timestamp', 'nid'))
    ->fields('pc', array('chtext'))
    ->fields('u', array('name'))
    ->condition('pv.nid', $node->nid)
    ->limit($votes_per_page)
    ->orderByHeader($header)
    ->execute();

  $rows = array();
  foreach ($queried_votes as $vote) {
    $rows[] = array(
      $vote->name ? theme('username', array('account' => $vote)) : check_plain($vote->hostname),
      check_plain($vote->chtext),
      format_date($vote->timestamp),
    );
  }
  $build['poll_votes_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#prefix' => t('This table lists all the recorded votes for this poll. If anonymous users are allowed to vote, they will be identified by the IP address of the computer they used when they voted.'),
  );
  $build['poll_votes_pager'] = array('#theme' => 'pager');
  return $build;
}
```

---
_Drupal 7.103 · [modules/poll/poll.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
