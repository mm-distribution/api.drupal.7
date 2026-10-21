# includes/mail.inc

- **Source:** [local](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · 684 lines

## File documentation

```text
@file
API functions for processing and sending e-mail.
```

## Functions (derived index)

- [drupal_mail()](drupal_mail.md) — Composes and optionally sends an e-mail message.
- [drupal_mail_system()](drupal_mail_system.md) — Returns an object that implements the MailSystemInterface interface.
- [drupal_wrap_mail()](drupal_wrap_mail.md) — Performs format=flowed soft wrapping for mail (RFC 3676).
- [drupal_html_to_text()](drupal_html_to_text.md) — Transforms an HTML string into plain text, preserving its structure.
- [drupal_mail_format_display_name()](drupal_mail_format_display_name.md) — Return a RFC-2822 compliant "display-name" component.
- [_drupal_wrap_mail_line()](_drupal_wrap_mail_line.md) — Wraps words on a single line.
- [_drupal_html_to_mail_urls()](_drupal_html_to_mail_urls.md) — Keeps track of URLs and replaces them with placeholder tokens.
- [_drupal_html_to_text_clean()](_drupal_html_to_text_clean.md) — Replaces non-quotation markers from a given piece of indentation with spaces.
- [_drupal_html_to_text_pad()](_drupal_html_to_text_pad.md) — Pads the last line with the given character.

## Classes and interfaces (derived index)

- [MailSystemInterface](MailSystemInterface.md) — An interface for pluggable mail back-ends.

## Constants

### MAIL_LINE_ENDINGS

- Line 13

```php
define('MAIL_LINE_ENDINGS', isset($_SERVER['WINDIR']) || (isset($_SERVER['SERVER_SOFTWARE']) && strpos($_SERVER['SERVER_SOFTWARE'], 'Win32') !== FALSE) ? "\r\n" : "\n");
```

```text
Auto-detect appropriate line endings for e-mails.

$conf['mail_line_endings'] will override this setting.
```

### MAIL_RFC_2822_SPECIALS

- Line 19

```php
define('MAIL_RFC_2822_SPECIALS', '()<>[]:;@\,."');
```

```text
Special characters, defined in RFC_2822.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
