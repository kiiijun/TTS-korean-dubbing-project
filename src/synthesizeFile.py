import argparse


def synthesize_ssml_file(ssml_file):
    #Synthesizes speech from the input file of ssml.

    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    with open(ssml_file, "r") as f:
        ssml = f.read()
        input_text = texttospeech.SynthesisInput(ssml=ssml)

    #voice => language = korean , voice Type = male    
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )
    #encoding -> .MP3 
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    #make "dubbing.mp3" file and write data.
    with open("dubbing.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "dubbing.mp3"')




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ssml", help="The ssml file from which to synthesize speech.")

    args = parser.parse_args()

    if args.ssml:
        synthesize_ssml_file(args.ssml)
