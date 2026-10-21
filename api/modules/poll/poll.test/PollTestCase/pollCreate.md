# PollTestCase::pollCreate()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 24–70 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L24-L70)
- **Class:** [PollTestCase](../PollTestCase.md)
- **Module/theme:** poll

## Signature

```php
function pollCreate($title, $choices, $preview = TRUE)
```

## Documentation

```text
Creates a poll.

@param string $title
  The title of the poll.
@param array $choices
  A list of choice labels.
@param boolean $preview
  (optional) Whether to test if the preview is working or not. Defaults to
  TRUE.

@return
  The node id of the created poll, or FALSE on error.
```

## Code

```php
  function pollCreate($title, $choices, $preview = TRUE) {
    $this->assertTrue(TRUE, 'Create a poll');

    $admin_user = $this->drupalCreateUser(array('create poll content', 'administer nodes'));
    $web_user = $this->drupalCreateUser(array('create poll content', 'access content', 'edit own poll content'));
    $this->drupalLogin($admin_user);

    // Get the form first to initialize the state of the internal browser.
    $this->drupalGet('node/add/poll');

    // Prepare a form with two choices.
    list($edit, $index) = $this->_pollGenerateEdit($title, $choices);

    // Verify that the vote count element only allows non-negative integers.
    $edit['choice[new:1][chvotes]'] = -1;
    $edit['choice[new:0][chvotes]'] = $this->randomString(7);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertText(t('Negative values are not allowed.'));
    $this->assertText(t('Vote count for new choice must be an integer.'));

    // Repeat steps for initializing the state of the internal browser.
    $this->drupalLogin($web_user);
    $this->drupalGet('node/add/poll');
    list($edit, $index) = $this->_pollGenerateEdit($title, $choices);

    // Re-submit the form until all choices are filled in.
    if (count($choices) > 2) {
      while ($index < count($choices)) {
        $this->drupalPost(NULL, $edit, t('More choices'));
        $this->assertPollChoiceOrder($choices, $index);
        list($edit, $index) = $this->_pollGenerateEdit($title, $choices, $index);
      }
    }

    if ($preview) {
      $this->drupalPost(NULL, $edit, t('Preview'));
      $this->assertPollChoiceOrder($choices, $index, TRUE);
      list($edit, $index) = $this->_pollGenerateEdit($title, $choices, $index);
    }

    $this->drupalPost(NULL, $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($title);
    $this->assertText(t('@type @title has been created.', array('@type' => node_type_get_name('poll'), '@title' => $title)), 'Poll has been created.');
    $this->assertTrue($node->nid, 'Poll has been found in the database.');

    return isset($node->nid) ? $node->nid : FALSE;
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
