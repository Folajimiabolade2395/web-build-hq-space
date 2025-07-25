
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs=e_mail,
        msg=f"Subject:{unconfirmed_person.verification_code} is your verification code for WebBuildHQ\n\n"
            f"Dear user,\n\nYour verification code is {unconfirmed_person.verification_code}. Please "
            f"note that it will expire in 14 minutes.\n\nBest Regards,\nWebBuildHQ"
    )


    # with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
    #     connection.starttls()
    #     connection.login("era99@ethereal.email", "vqr3dG8HWUHu23AMhY")
    #     connection.sendmail(
    #         from_addr="reply@webbuildhq.com",
    #         to_addrs=e_mail,
    #         msg=f"Subject:Password reset for WebBuildHQ account ({password_changer.verification_code})\n\n"
    #             f"Dear user,\n\nYour verification code to use in changing your password "
    #             f"is {password_changer.verification_code}. Please note it will expire in "
    #             f"14 minutes.\n\nBest Regards,\nWebBuildHQ"
    #     )