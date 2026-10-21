# TriggerActionTestCase::generateTokenExpandedComparison()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 291–306 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L291-L306)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function generateTokenExpandedComparison($trigger, $account)
```

## Documentation

```text
Generates a comparison message to match the pre-token-replaced message.

@param $trigger
  Trigger, like 'user_login'.
@param $account
  Associated user account.

@return
  The token-replaced equivalent message. This does not use token
  functionality.

@see generateMessageWithTokens()
```

## Code

```php
  function generateTokenExpandedComparison($trigger, $account) {
    // Note that user:last-login was omitted because it changes and can't
    // be properly verified.
    $message = t('Action was triggered by trigger @trigger user:name=@username user:uid=@uid user:mail=@mail user:url=@user_url user:edit-url=@user_edit_url user:created=@user_created',
       array(
        '@trigger' => $trigger,
        '@username' => $account->name,
        '@uid' => !empty($account->uid) ? $account->uid : t('not yet assigned'),
        '@mail' => $account->mail,
        '@user_url' => !empty($account->uid) ? url("user/$account->uid", array('absolute' => TRUE)) : t('not yet assigned'),
        '@user_edit_url' => !empty($account->uid) ? url("user/$account->uid/edit", array('absolute' => TRUE)) : t('not yet assigned'),
        '@user_created' => isset($account->created) ? format_date($account->created, 'medium') : t('not yet created'),
        )
      );
      return trim($message);
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
