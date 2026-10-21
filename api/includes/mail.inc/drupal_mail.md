# drupal_mail()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 128–204 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L128-L204)

## Signature

```php
function drupal_mail($module, $key, $to, $language, $params = array(), $from = NULL, $send = TRUE)
```

## Documentation

```text
Composes and optionally sends an e-mail message.

Sending an e-mail works with defining an e-mail template (subject, text
and possibly e-mail headers) and the replacement values to use in the
appropriate places in the template. Processed e-mail templates are
requested from hook_mail() from the module sending the e-mail. Any module
can modify the composed e-mail message array using hook_mail_alter().
Finally drupal_mail_system()->mail() sends the e-mail, which can
be reused if the exact same composed e-mail is to be sent to multiple
recipients.

Finding out what language to send the e-mail with needs some consideration.
If you send e-mail to a user, her preferred language should be fine, so
use user_preferred_language(). If you send email based on form values
filled on the page, there are two additional choices if you are not
sending the e-mail to a user on the site. You can either use the language
used to generate the page ($language global variable) or the site default
language. See language_default(). The former is good if sending e-mail to
the person filling the form, the later is good if you send e-mail to an
address previously set up (like contact addresses in a contact form).

Taking care of always using the proper language is even more important
when sending e-mails in a row to multiple users. Hook_mail() abstracts
whether the mail text comes from an administrator setting or is
static in the source code. It should also deal with common mail tokens,
only receiving $params which are unique to the actual e-mail at hand.

An example:

@code
  function example_notify($accounts) {
    foreach ($accounts as $account) {
      $params['account'] = $account;
      // example_mail() will be called based on the first drupal_mail() parameter.
      drupal_mail('example', 'notice', $account->mail, user_preferred_language($account), $params);
    }
  }

  function example_mail($key, &$message, $params) {
    $data['user'] = $params['account'];
    $options['language'] = $message['language'];
    user_mail_tokens($variables, $data, $options);
    switch($key) {
      case 'notice':
        // If the recipient can receive such notices by instant-message, do
        // not send by email.
        if (example_im_send($key, $message, $params)) {
          $message['send'] = FALSE;
          break;
        }
        $langcode = $message['language']->language;
        $message['subject'] = t('Notification from !site', $variables, array('langcode' => $langcode));
        $message['body'][] = t("Dear !username\n\nThere is new content available on the site.", $variables, array('langcode' => $langcode));
        break;
    }
  }
@endcode

Another example, which uses drupal_mail() to format a message for sending
later:

@code
  $params = array('current_conditions' => $data);
  $to = 'user@example.com';
  $message = drupal_mail('example', 'notice', $to, $language, $params, FALSE);
  // Only add to the spool if sending was not canceled.
  if ($message['send']) {
    example_spool_message($message);
  }
@endcode

@param $module
  A module name to invoke hook_mail() on. The {$module}_mail() hook will be
  called to complete the $message structure which will already contain common
  defaults.
@param $key
  A key to identify the e-mail sent. The final e-mail id for e-mail altering
  will be {$module}_{$key}.
@param $to
  The e-mail address or addresses where the message will be sent to. The
  formatting of this string will be validated with the
  @link http://php.net/manual/filter.filters.validate.php PHP e-mail validation filter. @endlink
  Some examples are:
  - user@example.com
  - user@example.com, anotheruser@example.com
  - User <user@example.com>
  - User <user@example.com>, Another User <anotheruser@example.com>
@param $language
  Language object to use to compose the e-mail.
@param $params
  Optional parameters to build the e-mail.
@param $from
  Sets From to this value, if given.
@param $send
  If TRUE, drupal_mail() will call drupal_mail_system()->mail() to deliver
  the message, and store the result in $message['result']. Modules
  implementing hook_mail_alter() may cancel sending by setting
  $message['send'] to FALSE.

@return
  The $message array structure containing all details of the
  message. If already sent ($send = TRUE), then the 'result' element
  will contain the success indicator of the e-mail, failure being already
  written to the watchdog. (Success means nothing more than the message being
  accepted at php-level, which still doesn't guarantee it to be delivered.)
```

## Code

```php
function drupal_mail($module, $key, $to, $language, $params = array(), $from = NULL, $send = TRUE) {
  $default_from = variable_get('site_mail', ini_get('sendmail_from'));

  // Bundle up the variables into a structured array for altering.
  $message = array(
    'id'       => $module . '_' . $key,
    'module'   => $module,
    'key'      => $key,
    'to'       => $to,
    'from'     => isset($from) ? $from : $default_from,
    'language' => $language,
    'params'   => $params,
    'send'     => TRUE,
    'subject'  => '',
    'body'     => array()
  );

  // Build the default headers
  $headers = array(
    'MIME-Version'              => '1.0',
    'Content-Type'              => 'text/plain; charset=UTF-8; format=flowed; delsp=yes',
    'Content-Transfer-Encoding' => '8Bit',
    'X-Mailer'                  => 'Drupal'
  );
  if ($default_from) {
    // To prevent e-mail from looking like spam, the addresses in the Sender and
    // Return-Path headers should have a domain authorized to use the originating
    // SMTP server.
    $headers['From'] = $headers['Sender'] = $headers['Return-Path'] = $default_from;

    if (variable_get('mail_display_name_site_name', FALSE)) {
      $display_name = variable_get('site_name', 'Drupal');
      $headers['From'] = drupal_mail_format_display_name($display_name) . ' <' . $default_from . '>';
    }
  }
  if ($from && $from != $default_from) {
    $headers['From'] = $from;
  }
  $message['headers'] = $headers;

  // Build the e-mail (get subject and body, allow additional headers) by
  // invoking hook_mail() on this module. We cannot use module_invoke() as
  // we need to have $message by reference in hook_mail().
  if (function_exists($function = $module . '_mail')) {
    $function($key, $message, $params);
  }

  // Invoke hook_mail_alter() to allow all modules to alter the resulting e-mail.
  drupal_alter('mail', $message);

  // Retrieve the responsible implementation for this message.
  $system = drupal_mail_system($module, $key);

  // Format the message body.
  $message = $system->format($message);

  // Optionally send e-mail.
  if ($send) {
    // The original caller requested sending. Sending was canceled by one or
    // more hook_mail_alter() implementations. We set 'result' to NULL, because
    // FALSE indicates an error in sending.
    if (empty($message['send'])) {
      $message['result'] = NULL;
    }
    // Sending was originally requested and was not canceled.
    else {
      $message['result'] = $system->mail($message);
      // Log errors.
      if (!$message['result']) {
        watchdog('mail', 'Error sending e-mail (from %from to %to).', array('%from' => $message['from'], '%to' => $message['to']), WATCHDOG_ERROR);
        drupal_set_message(t('Unable to send e-mail. Contact the site administrator if the problem persists.'), 'error');
      }
    }
  }

  return $message;
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
