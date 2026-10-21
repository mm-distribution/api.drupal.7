# PollTokenReplaceTestCase::testPollTokenReplacement()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 643–710 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L643-L710)
- **Class:** [PollTokenReplaceTestCase](../PollTokenReplaceTestCase.md)
- **Module/theme:** poll

## Signature

```php
function testPollTokenReplacement()
```

## Documentation

```text
Creates a poll, then tests the tokens generated from it.
```

## Code

```php
  function testPollTokenReplacement() {
    global $language;

    // Craete a poll with three choices.
    $title = $this->randomName();
    $choices = $this->_generateChoices(3);
    $poll_nid = $this->pollCreate($title, $choices, FALSE);
    $this->drupalLogout();

    // Create four users and have each of them vote.
    $vote_user1 = $this->drupalCreateUser(array('vote on polls', 'access content'));
    $this->drupalLogin($vote_user1);
    $edit = array(
      'choice' => '1',
    );
    $this->drupalPost('node/' . $poll_nid, $edit, t('Vote'));
    $this->drupalLogout();

    $vote_user2 = $this->drupalCreateUser(array('vote on polls', 'access content'));
    $this->drupalLogin($vote_user2);
    $edit = array(
      'choice' => '1',
    );
    $this->drupalPost('node/' . $poll_nid, $edit, t('Vote'));
    $this->drupalLogout();

    $vote_user3 = $this->drupalCreateUser(array('vote on polls', 'access content'));
    $this->drupalLogin($vote_user3);
    $edit = array(
      'choice' => '2',
    );
    $this->drupalPost('node/' . $poll_nid, $edit, t('Vote'));
    $this->drupalLogout();

    $vote_user4 = $this->drupalCreateUser(array('vote on polls', 'access content'));
    $this->drupalLogin($vote_user4);
    $edit = array(
      'choice' => '3',
    );
    $this->drupalPost('node/' . $poll_nid, $edit, t('Vote'));
    $this->drupalLogout();

    $poll = node_load($poll_nid, NULL, TRUE);

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[node:poll-votes]'] = 4;
    $tests['[node:poll-winner]'] = filter_xss($poll->choice[1]['chtext']);
    $tests['[node:poll-winner-votes]'] = 2;
    $tests['[node:poll-winner-percent]'] = 50;
    $tests['[node:poll-duration]'] = format_interval($poll->runtime, 1, $language->language);

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $poll), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized poll token %token replaced.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[node:poll-winner]'] = $poll->choice[1]['chtext'];

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $poll), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized poll token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
