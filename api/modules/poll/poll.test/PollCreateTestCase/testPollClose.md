# PollCreateTestCase::testPollClose()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 238–287 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L238-L287)
- **Class:** [PollCreateTestCase](../PollCreateTestCase.md)
- **Module/theme:** poll

## Signature

```php
function testPollClose()
```

## Documentation

_No docblock in source._

## Code

```php
  function testPollClose() {
    $content_user = $this->drupalCreateUser(array('create poll content', 'edit any poll content', 'access content'));
    $vote_user = $this->drupalCreateUser(array('cancel own vote', 'inspect all votes', 'vote on polls', 'access content'));

    // Create poll.
    $title = $this->randomName();
    $choices = $this->_generateChoices(7);
    $poll_nid = $this->pollCreate($title, $choices, FALSE);

    $this->drupalLogout();
    $this->drupalLogin($content_user);

    // Edit the poll node and close the poll.
    $close_edit = array('active' => 0);
    $this->pollUpdate($poll_nid, $title, $close_edit);

    // Verify 'Vote' button no longer appears.
    $this->drupalGet('node/' . $poll_nid);
    $elements = $this->xpath('//input[@id="edit-vote"]');
    $this->assertTrue(empty($elements), "Vote button doesn't appear.");

    // Verify status on 'poll' page is 'closed'.
    $this->drupalGet('poll');
    $this->assertText($title, 'Poll appears in poll list.');
    $this->assertText('closed', 'Poll is closed.');

    // Edit the poll node and re-activate.
    $open_edit = array('active' => 1);
    $this->pollUpdate($poll_nid, $title, $open_edit);

    // Vote on the poll.
    $this->drupalLogout();
    $this->drupalLogin($vote_user);
    $vote_edit = array('choice' => '1');
    $this->drupalPost('node/' . $poll_nid, $vote_edit, t('Vote'));
    $this->assertText('Your vote was recorded.', 'Your vote was recorded.');
    $elements = $this->xpath('//input[@value="Cancel your vote"]');
    $this->assertTrue(isset($elements[0]), "'Cancel your vote' button appears.");

    // Edit the poll node and close the poll.
    $this->drupalLogout();
    $this->drupalLogin($content_user);
    $close_edit = array('active' => 0);
    $this->pollUpdate($poll_nid, $title, $close_edit);

    // Verify 'Cancel your vote' button no longer appears.
    $this->drupalGet('node/' . $poll_nid);
    $elements = $this->xpath('//input[@value="Cancel your vote"]');
    $this->assertTrue(empty($elements), "'Cancel your vote' button no longer appears.");
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
