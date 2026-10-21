# PollJSAddChoice::testAddChoice()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 458–476 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L458-L476)
- **Class:** [PollJSAddChoice](../PollJSAddChoice.md)
- **Module/theme:** poll

## Signature

```php
function testAddChoice()
```

## Documentation

```text
Test adding a new choice.
```

## Code

```php
  function testAddChoice() {
    $web_user = $this->drupalCreateUser(array('create poll content', 'access content'));
    $this->drupalLogin($web_user);
    $this->drupalGet('node/add/poll');
    $edit = array(
      "title" => $this->randomName(),
      'choice[new:0][chtext]' => $this->randomName(),
      'choice[new:1][chtext]' => $this->randomName(),
    );

    // Press 'add choice' button through Ajax, and place the expected HTML result
    // as the tested content.
    $commands = $this->drupalPostAJAX(NULL, $edit, array('op' => t('More choices')));
    $this->content = $commands[1]['data'];

    $this->assertFieldByName('choice[chid:0][chtext]', $edit['choice[new:0][chtext]'], format_string('Field !i found', array('!i' => 0)));
    $this->assertFieldByName('choice[chid:1][chtext]', $edit['choice[new:1][chtext]'], format_string('Field !i found', array('!i' => 1)));
    $this->assertFieldByName('choice[new:0][chtext]', '', format_string('Field !i found', array('!i' => 2)));
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
