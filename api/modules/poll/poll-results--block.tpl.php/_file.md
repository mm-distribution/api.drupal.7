# modules/poll/poll-results--block.tpl.php

- **Source:** [local](../../../../source/modules/poll/poll-results--block.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll-results--block.tpl.php) · 29 lines
- **Module/theme:** poll

## File documentation

```text
@file
Default theme implementation to display the poll results in a block.

Variables available:
- $title: The title of the poll.
- $results: The results of the poll.
- $votes: The total results in the poll.
- $links: Links in the poll.
- $nid: The nid of the poll
- $cancel_form: A form to cancel the user's vote, if allowed.
- $raw_links: The raw array of links. Should be run through theme('links')
  if used.
- $vote: The choice number of the current user's vote.

@see template_preprocess_poll_results()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
