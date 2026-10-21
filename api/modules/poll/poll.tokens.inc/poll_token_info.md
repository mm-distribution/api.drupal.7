# poll_token_info()

- **Type:** Function
- **File:** [`modules/poll/poll.tokens.inc`](_file.md), lines 11–36 · [local source](../../../../source/modules/poll/poll.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.tokens.inc#L11-L36)
- **Module/theme:** poll
- **Implements:** [hook_token_info()](../../system/system.api.php/hook_token_info.md)

## Signature

```php
function poll_token_info()
```

## Documentation

```text
Implements hook_token_info().
```

## Code

```php
function poll_token_info() {
  $node['poll-votes'] = array(
    'name' => t("Poll votes"),
    'description' => t("The number of votes that have been cast on a poll."),
  );
  $node['poll-winner'] = array(
    'name' => t("Poll winner"),
    'description' => t("The winning poll answer."),
  );
  $node['poll-winner-votes'] = array(
    'name' => t("Poll winner votes"),
    'description' => t("The number of votes received by the winning poll answer."),
  );
  $node['poll-winner-percent'] = array(
    'name' => t("Poll winner percent"),
    'description' => t("The percentage of votes received by the winning poll answer."),
  );
  $node['poll-duration'] = array(
    'name' => t("Poll duration"),
    'description' => t("The length of time the poll is set to run."),
  );

  return array(
    'tokens' => array('node' => $node),
  );
}
```

---
_Drupal 7.103 · [modules/poll/poll.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
